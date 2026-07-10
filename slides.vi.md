---
marp: true
theme: rio
title: Rio — Kỹ sư bảo trì phần mềm AI (VI)
description: Customer pitch deck for Rio (10-minute, multi-prospect webinar)
paginate: true
---

<!--
HOW TO PRESENT / BUILD
----------------------
Live preview server (auto-reloads on edit):
  npx @marp-team/marp-cli -s . --html --theme-set theme/rio.css
Export:
  npx @marp-team/marp-cli slides.md -o dist/rio-deck.html --html --theme-set theme/rio.css
  npx @marp-team/marp-cli slides.md --pdf --theme-set theme/rio.css

FORMAT: 10 minutes · MANY prospects at once (broadcast, not 1:1).
Each `---` is a slide. Comments starting with ⏱ are SPEAKER NOTES (presenter
view only); comments starting with `_class:` are Marp layout directives.
-->

<!-- _class: title -->

<div class="title-row">
  <img src="assets/robot.svg" alt="Rio">
  <div>
    <div class="brand-row"><span class="brand">Rio</span><span class="eyebrow">Kỹ sư bảo trì phần mềm AI</span></div>
    <h1>Nhắn một câu.<br><em>Phần mềm của bạn được ship.</em></h1>
  </div>
</div>

<p class="sub">Kỹ sư AI bảo trì codebase của bạn <strong>ngay cả khi bạn ngủ</strong> — tất cả từ điện thoại. Bạn gõ yêu cầu, <strong>bạn duyệt</strong>, Rio ship.</p>

<p class="url">https://rio.sotatek.kr</p>

<!--
⏱ 0:00–0:45 — TITLE / HOOK
"Imagine fixing your live product by sending one chat message — and still
approving everything before it goes out. That's Rio."
Let people settle. One strong sentence, then move on.
-->

---

<span class="eyebrow">Một vấn đề quen thuộc</span>

## Chỉnh sửa nhỏ, chờ cả tuần.

<p class="muted">Bạn không thiếu ý tưởng — bạn thiếu một đội kỹ thuật rảnh tay cho những việc “nhỏ mà gấp”.</p>

<div class="stats">
  <div class="stat"><div class="k">3–7 ngày</div><p>để ship một dòng sửa.</p></div>
  <div class="stat"><div class="k">“Nhanh thôi mà…”</div><p>trôi trong ticket &amp; họp hành.</p></div>
  <div class="stat"><div class="k">Không kiểm soát</div><p>với thứ AI tự ý đẩy đi.</p></div>
</div>

<!--
⏱ 0:45–2:00 — THE PAIN
Broadcast poll: "Show of hands / yes in chat — who has a one-line change stuck
in a queue right now?" Wait 3 seconds, acknowledge, move on. The nods sell it.
-->

---

<div class="cols">
<div>

<span class="eyebrow">Gặp Rio</span>

## Một đồng đội AI, bạn nắm quyền.

- Mô tả thay đổi bằng **lời thường** — không ticket, không thuật ngữ
- Chạy **thẳng trên repo của bạn** (GitHub App an toàn)
- Mọi lần phát hành đều qua **cổng duyệt của con người**
- **24/7** — gửi lúc nửa đêm, sáng ra đã có bản chờ duyệt

> Tự động vận hành. Con người kiểm soát.

</div>
<div style="text-align:center">
  <img src="assets/robot.svg" alt="Rio" style="width:200px;height:200px;border-radius:44px;box-shadow:0 0 70px 8px rgba(124,127,248,.4)">
</div>
</div>

<!--
⏱ 2:00–3:00 — POSITIONING
Land the frame BEFORE the mechanics: not "an AI that codes" — "an AI teammate
that maintains your product, with you in charge." Say the tagline out loud.
-->

---

<span class="eyebrow">Cách hoạt động — hai cổng là của bạn</span>

## Năm bước tự động. Hai bước là của bạn.

<div class="flow">
  <div class="node"><div class="dot">1</div><div class="lb">Gửi yêu cầu</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">2</div><div class="lb">Rio phân tích</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">3</div><div class="lb">Duyệt kế hoạch</div><div class="who">⏸ BẠN</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">4</div><div class="lb">Code trên dev</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">5</div><div class="lb">Test + xem thử</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">6</div><div class="lb">Duyệt merge</div><div class="who">⏸ QUẢN LÝ</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">7</div><div class="lb">Ship + báo cáo</div></div>
</div>

<!--
⏱ 3:00–4:30 — THE FLOW
Don't narrate all 7. "Five are automatic. Two are yours" — point at 3 and 6.
That contrast is the whole story.
-->

---

<span class="eyebrow">Hai cổng duyệt = quyền kiểm soát</span>

## Rio không bao giờ tự ý ship. Không bao giờ.

<div class="gates">
  <div class="gatecard">
    <div class="g">⏸ CỔNG 1 · BẠN</div>
    <h3>Bạn duyệt kế hoạch</h3>
    <p>Trước khi Rio viết một dòng, bạn thấy nó sẽ làm <em>gì</em> và <em>vì sao</em>. Trả lời “ok”, hoặc chỉnh lại.</p>
  </div>
  <div class="gatecard">
    <div class="g">⏸ CỔNG 2 · QUẢN LÝ</div>
    <h3>Quản lý duyệt merge</h3>
    <p>Chỉ người có quyền bấm nút cuối. Không ai khác chạm vào <code>main</code>.</p>
  </div>
</div>

<!--
⏱ 4:30–5:15 — TRUST (objection-killer)
This slide disarms the #1 fear: "AI touching our live code." Say the headline
slowly and literally. Pause. Then move into why teams trust it.
-->

---

<span class="eyebrow">Vì sao các đội tin Rio</span>

## Không phải con bot tự tung tự tác.

<div class="tiles">
  <div class="tile g"><div class="ic">⏸</div><h3>Hai cổng duyệt</h3><p>Kế hoạch + merge, không bỏ qua.</p></div>
  <div class="tile"><div class="ic">◇</div><h3>Repo của chính bạn</h3><p>GitHub App an toàn — code không rời repo.</p></div>
  <div class="tile"><div class="ic">◷</div><h3>24/7, không xếp hàng</h3><p>Không ticket, không họp.</p></div>
  <div class="tile"><div class="ic">⌥</div><h3>Nhánh dev an toàn</h3><p>Được test &amp; xem thử trước production.</p></div>
  <div class="tile"><div class="ic">✎</div><h3>Ngôn ngữ của bạn</h3><p>Nhập lời thường, nhận ngôn ngữ nghiệp vụ — EN · VI · KO.</p></div>
  <div class="tile"><div class="ic">◱</div><h3>Đa tenant</h3><p>Không gian riêng, cách ly cho mỗi khách.</p></div>
</div>

<!--
⏱ 5:15–6:15 — WHY TRUST
Mixed audience → SPEAK ONLY the top row (two gates · your own repo · 24/7).
One sentence for the rest: "…plus your dev branch, your language, full tenant
isolation." Let the slide carry them.
-->

---

<span class="eyebrow">Đa kênh</span>

## Dùng chính app chat bạn đang có.

<p class="muted">Không công cụ mới. Không thói quen mới. Cá nhân hay nhóm — một thread = một yêu cầu.</p>

<div class="chips">
  <span class="chip"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#29A9EA"/><path fill="#fff" d="M5.5 11.7l11.2-4.3c.5-.2 1 .1.8.9l-1.9 9c-.1.5-.5.7-.9.4l-2.6-1.9-1.3 1.2c-.1.1-.3.2-.5.2l.2-2.7 4.9-4.4c.2-.2 0-.3-.3-.1l-6 3.8-2.6-.8c-.6-.2-.6-.6.1-.9z"/></svg>Telegram</span>
  <span class="chip"><svg viewBox="0 0 24 24"><path fill="#00AC47" d="M4 3h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-8l-5 4v-4H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/></svg>Google Chat</span>
  <span class="chip"><svg viewBox="0 0 24 24"><rect x="10" y="2" width="4" height="9" rx="2" fill="#36C5F0"/><rect x="13" y="10" width="9" height="4" rx="2" fill="#2EB67D"/><rect x="10" y="13" width="4" height="9" rx="2" fill="#ECB22E"/><rect x="2" y="10" width="9" height="4" rx="2" fill="#E01E5A"/></svg>Slack</span>
  <span class="chip"><svg viewBox="0 0 24 24"><defs><linearGradient id="msg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00B2FF"/><stop offset="1" stop-color="#0068FF"/></linearGradient></defs><path fill="url(#msg)" d="M12 2C6.2 2 2 6.4 2 12.1c0 3 1.3 5.6 3.4 7.3V23l3.2-1.8c.8.2 1.6.3 2.4.3 5.8 0 10-4.4 10-10.1S17.8 2 12 2z"/><path fill="#fff" d="M6.4 14.6l2.9-4.6 2.6 2 2.4-2.6-2.9 4.5-2.5-1.9z"/></svg>Messenger</span>
  <span class="chip"><svg viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#0068FF"/><path fill="#fff" d="M12 6.2c-3.2 0-5.8 2.1-5.8 4.8 0 1.5.8 2.9 2.1 3.8L7.7 17l2.5-1.3c.6.1 1.2.2 1.8.2 3.2 0 5.8-2.1 5.8-4.8S15.2 6.2 12 6.2z"/></svg>Zalo</span>
</div>

<p class="soon">Sắp có — <strong>Microsoft Teams · KakaoTalk · Naver Works</strong></p>

<!--
⏱ 6:15–7:00 — REACH
Broadcast: "Whatever your team lives in — one of these is almost certainly it."
Sweep across the logos. Call out KakaoTalk / Zalo if the room is KR / VN.
-->

---

<span class="eyebrow">Bắt đầu</span>

## Chạy trong hai phút.

<div class="steps">
  <div class="step"><div class="b">1</div><div><h3>Kết nối repo</h3><p>Cấp quyền GitHub App an toàn — code không rời repo.</p></div></div>
  <div class="step"><div class="b">2</div><div><h3>Mời Rio vào chat</h3><p>Cá nhân hay nhóm, kênh nào cũng được.</p></div></div>
  <div class="step"><div class="b">3</div><div><h3>Gửi yêu cầu đầu tiên — từ điện thoại</h3><p>Gõ. Chạm duyệt. Xem nó ship.</p></div></div>
</div>

<!--
⏱ 7:00–7:30 — LOW-RISK ONBOARDING
Make it feel small and reversible: "Two minutes, one repo — try it on a
throwaway change first. Nothing goes live without your tap."
-->

---

<!-- _class: demo -->

<div class="cols demo">
<div>

<span class="eyebrow">🔴 Demo trực tiếp</span>

## Từ điện thoại, trong Google Chat.

<p class="muted">Một tin nhắn → kế hoạch bạn duyệt → link xem thử. Chưa tới một phút.</p>

</div>
<div>
  <div class="phone">
    <div class="screen">
      <div class="gc-head"><img src="assets/robot.svg"><div><div class="nm">Rio</div><div class="st">Đang hoạt động trong Google Chat</div></div></div>
      <div class="gc-body">
        <div class="gc-day">Hôm nay</div>
        <div class="bub out">Cho nút “Đăng ký” màu xanh và to hơn chút nhé 🙏</div>
        <div class="bub in"><div class="who">Rio</div>Rõ rồi — CTA sang xanh thương hiệu, to hơn. Đây là kế hoạch — duyệt trước khi tôi ship nhé?</div>
        <div class="approve">⏸ Duyệt kế hoạch</div>
        <div class="bub out">ok, làm luôn đi ✅</div>
        <div class="bub in"><div class="who">Rio</div>Xong trên <b>dev</b>, test pass. Bản xem thử sẵn sàng 🚀</div>
      </div>
    </div>
  </div>
</div>
</div>

<!--
⏱ 7:30–9:15 — LIVE DEMO (the finale, right before the ask)
Do it live if possible: real chat → plan → approve → preview link. Pre-load a
repo and a rehearsed change. If risky in a big webinar, play a screen recording
here instead. Narrate the two gates — then go straight to the closing ask.
-->

---

<!-- _class: close -->

# Giao bảo trì cho Rio.<br>Giữ quyền quyết định.

<p class="cta"><strong>Đặt lịch 20 phút</strong> — cùng kết nối một repo và chạy thử một thay đổi trực tiếp.</p>

<p class="url">https://rio.sotatek.kr</p>

<!--
⏱ 9:15–10:00 — CLOSE WITH THE ASK
One clear next step for the whole room: "Drop your email / scan this — we'll
book 20 minutes to connect one repo and run a real change this week."
End on the ask, not "thank you". Then open Q&A.
-->
