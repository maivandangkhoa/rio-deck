import os
import smtplib
import ssl
import sys
from dataclasses import dataclass
from email.message import EmailMessage
from email.utils import parsedate_to_datetime
from urllib.parse import quote_plus
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


@dataclass
class News:
    title: str
    link: str
    source: str
    published: str


def fetch_rss(query: str) -> list[News]:
    url = (
        "https://news.google.com/rss/search?q="
        + quote_plus(query)
        + "&hl=ko&gl=KR&ceid=KR:ko"
    )
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 SeoulNewsBot/1.0"})
    with urlopen(req, timeout=30) as response:
        xml = response.read()
    root = ET.fromstring(xml)
    items: list[News] = []
    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub = (item.findtext("pubDate") or "").strip()
        source_el = item.find("source")
        source = (source_el.text if source_el is not None else "Google News").strip()
        if title and link:
            items.append(News(title, link, source, pub))
    return items


def sort_key(news: News):
    try:
        return parsedate_to_datetime(news.published)
    except Exception:
        return parsedate_to_datetime("Thu, 01 Jan 1970 00:00:00 GMT")


def get_news(limit: int = 10) -> list[News]:
    queries = [
        "서울 최신 뉴스 when:1d",
        "Seoul latest news when:1d",
        "서울 관광 여행 행사 when:1d",
    ]
    merged: dict[str, News] = {}
    for query in queries:
        try:
            for item in fetch_rss(query):
                # Google News can return the same article for multiple queries.
                merged.setdefault(item.link, item)
        except Exception as exc:
            print(f"RSS warning for {query}: {exc}", file=sys.stderr)
    return sorted(merged.values(), key=sort_key, reverse=True)[:limit]


def build_message(news: list[News]) -> str:
    lines = ["📰 Seoul — 10 tin mới nhất", "", "Nguồn: Google News RSS · Không sao chép nội dung bài viết"]
    for i, item in enumerate(news, 1):
        lines += [f"{i}. {item.title}", f"   {item.source} · {item.link}"]
    return "\n".join(lines)


def send_telegram(message: str) -> None:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    import json

    payload = json.dumps({"chat_id": chat_id, "text": message}).encode()
    req = Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=30) as response:
        if response.status >= 300:
            raise RuntimeError(f"Telegram returned HTTP {response.status}")


def send_email(message: str) -> None:
    host = os.environ["SMTP_HOST"]
    port = int(os.getenv("SMTP_PORT", "465"))
    username = os.environ["SMTP_USERNAME"]
    password = os.environ["SMTP_PASSWORD"]
    sender = os.environ.get("EMAIL_FROM", username)
    recipient = os.environ["EMAIL_TO"]

    email = EmailMessage()
    email["Subject"] = "Seoul — 10 tin mới nhất"
    email["From"] = sender
    email["To"] = recipient
    email.set_content(message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context, timeout=30) as smtp:
        smtp.login(username, password)
        smtp.send_message(email)


def send_zalo_webhook(message: str) -> None:
    """Optional Zalo bridge.

    Zalo OA credentials and permissions depend on the OA/app setup. To avoid
    hard-coding an account-specific endpoint, this sends JSON to a configured
    webhook. A small Zalo OA service can receive it and call Zalo's official API.
    """
    webhook = os.getenv("ZALO_WEBHOOK_URL")
    if not webhook:
        return
    import json

    payload = json.dumps({"message": message}).encode()
    req = Request(
        webhook,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=30) as response:
        if response.status >= 300:
            raise RuntimeError(f"Zalo webhook returned HTTP {response.status}")


def main() -> None:
    news = get_news(10)
    if not news:
        raise RuntimeError("No Seoul news found")
    message = build_message(news)

    channels = os.getenv("CHANNELS", "telegram").lower().split(",")
    for channel in channels:
        channel = channel.strip()
        if channel == "telegram":
            send_telegram(message)
        elif channel == "email":
            send_email(message)
        elif channel == "zalo":
            send_zalo_webhook(message)
        elif channel:
            raise ValueError(f"Unsupported channel: {channel}")

    print(message)


if __name__ == "__main__":
    main()
