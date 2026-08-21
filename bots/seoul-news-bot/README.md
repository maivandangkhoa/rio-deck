# Seoul News Bot

Runs every day at **08:00 Asia/Seoul** using GitHub Actions and sends the 10 newest Seoul-related headlines.

The workflow uses Google News RSS for discovery and sends headlines + source links only; it does not copy article bodies.

## Channels

Set `NEWS_CHANNELS` to one or more comma-separated values:

- `telegram`
- `email`
- `zalo` (via `ZALO_WEBHOOK_URL`)

Example: `telegram,email`

## GitHub Actions secrets

### Telegram

Create a bot with BotFather and add:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

The bot uses Telegram's official `sendMessage` API.

### Email

Add:

- `SMTP_HOST` (e.g. smtp.gmail.com)
- `SMTP_PORT` (usually 465 for SMTP SSL)
- `SMTP_USERNAME`
- `SMTP_PASSWORD` (use an app password where required)
- `EMAIL_FROM`
- `EMAIL_TO`

### Zalo

Zalo OA messaging requires an OA/app setup, token, recipient permissions and an account-specific API flow. This repo therefore exposes `ZALO_WEBHOOK_URL`: point it to a small service that receives `{"message":"..."}` and calls Zalo's official API with your OA credentials.

## Manual test

In GitHub: **Actions → Seoul News Bot → Run workflow**.

## Schedule

The workflow uses GitHub Actions' timezone-aware schedule:

```yaml
cron: '0 8 * * *'
timezone: 'Asia/Seoul'
```

GitHub notes that scheduled workflows can be delayed during periods of high Actions load, especially at the start of an hour. If exact 08:00 delivery becomes important, move the cron to `03 8 * * *` or use a dedicated scheduler.
