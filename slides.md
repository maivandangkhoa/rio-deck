---
marp: true
theme: rio
title: Rio — AI Maintenance Engineer
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
    <div class="brand-row"><span class="brand">Rio</span><span class="eyebrow">AI maintenance engineer</span></div>
    <h1>Message once.<br><em>Your software ships.</em></h1>
  </div>
</div>

<p class="sub">The AI engineer that maintains your codebase <strong>while you sleep</strong> — all from your phone. You type the change, <strong>you approve</strong>, Rio ships.</p>

<p class="url">https://rio.sotatek.kr</p>

<!--
⏱ 0:00–0:45 — TITLE / HOOK
"Imagine fixing your live product by sending one chat message — and still
approving everything before it goes out. That's Rio."
Let people settle. One strong sentence, then move on.
-->

---

<span class="eyebrow">A familiar problem</span>

## The small fix that waited a week.

<p class="muted">You never run out of ideas — you run out of an engineering team free for the “small but urgent” things.</p>

<div class="stats">
  <div class="stat"><div class="k">3–7 days</div><p>to ship a one-line change.</p></div>
  <div class="stat"><div class="k">“Quick one…”</div><p>lost in tickets &amp; meetings.</p></div>
  <div class="stat"><div class="k">Zero control</div><p>over what an AI would ship on its own.</p></div>
</div>

<!--
⏱ 0:45–2:00 — THE PAIN
Broadcast poll: "Show of hands / yes in chat — who has a one-line change stuck
in a queue right now?" Wait 3 seconds, acknowledge, move on. The nods sell it.
-->

---

<div class="cols">
<div>

<span class="eyebrow">Meet Rio</span>

## An AI teammate, with you in charge.

- Describe the change in **plain words** — no tickets, no jargon
- Works **directly on your own repository** (secure GitHub App)
- Every release passes **human approval gates**
- **24/7** — send at midnight, wake to a change ready for review

> Autonomous work. Human control.

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

<span class="eyebrow">How it works — two gates are yours</span>

## Five steps automatic. Two are yours.

<div class="flow">
  <div class="node"><div class="dot">1</div><div class="lb">Send request</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">2</div><div class="lb">Rio analyses</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">3</div><div class="lb">Approve plan</div><div class="who">⏸ YOU</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">4</div><div class="lb">Code on dev</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">5</div><div class="lb">Test + preview</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">6</div><div class="lb">Approve preview</div><div class="who">⏸ YOU</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">7</div><div class="lb">Approve merge</div><div class="who">⏸ MANAGER</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">8</div><div class="lb">Ship + report</div></div>
</div>

<!--
⏱ 3:00–4:30 — THE FLOW
Don't narrate all 8. "Five are automatic. Two are yours" — point at 3 and 6
(your gates), 7 is your manager's. That contrast is the whole story.
-->

---

<span class="eyebrow">The three gates = your control</span>

## Rio never ships unattended. Ever.

<div class="gates">
  <div class="gatecard">
    <div class="g">⏸ GATE 1 · YOU</div>
    <h3>You approve the plan</h3>
    <p>Before Rio writes a single line, you see <em>what</em> it will do and <em>why</em>. Reply “ok”, or refine it.</p>
  </div>
  <div class="gatecard">
    <div class="g">⏸ GATE 2 · YOU</div>
    <h3>You approve the dev preview</h3>
    <p>Rio ships to <code>dev</code> first. You open the preview link and confirm it’s right before anything goes further.</p>
  </div>
  <div class="gatecard">
    <div class="g">⏸ GATE 3 · MANAGER</div>
    <h3>A manager approves the merge</h3>
    <p>Only an authorised person clicks the final button. No one else ever touches <code>main</code>.</p>
  </div>
</div>

<!--
⏱ 4:30–5:15 — TRUST (objection-killer)
This slide disarms the #1 fear: "AI touching our live code." Say the headline
slowly and literally. Pause. Then move into why teams trust it.
-->

---

<span class="eyebrow">Why teams trust Rio</span>

## Not a bot on the loose.

<div class="tiles">
  <div class="tile g"><div class="ic">⏸</div><h3>Three approval gates</h3><p>Plan + preview + merge, never skipped.</p></div>
  <div class="tile"><div class="ic">◇</div><h3>Your own repo</h3><p>Secure GitHub App — code never leaves it.</p></div>
  <div class="tile"><div class="ic">◷</div><h3>24/7, no queue</h3><p>No tickets, no meetings.</p></div>
  <div class="tile"><div class="ic">⌥</div><h3>Safe dev branch</h3><p>Tested &amp; previewed before production.</p></div>
  <div class="tile"><div class="ic">✎</div><h3>Your language</h3><p>Plain words in, business terms out — EN · VI · KO.</p></div>
  <div class="tile"><div class="ic">◱</div><h3>Multi-tenant</h3><p>A private, isolated space per client.</p></div>
</div>

<!--
⏱ 5:15–6:15 — WHY TRUST
Mixed audience → SPEAK ONLY the top row (two gates · your own repo · 24/7).
One sentence for the rest: "…plus your dev branch, your language, full tenant
isolation." Let the slide carry them.
-->

---

<span class="eyebrow">Multi-channel</span>

## Use the chat app you already have.

<p class="muted">No new tools. No new habits. Personal or group — one thread = one request.</p>

<div class="chips">
  <span class="chip"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#29A9EA"/><path fill="#fff" d="M5.5 11.7l11.2-4.3c.5-.2 1 .1.8.9l-1.9 9c-.1.5-.5.7-.9.4l-2.6-1.9-1.3 1.2c-.1.1-.3.2-.5.2l.2-2.7 4.9-4.4c.2-.2 0-.3-.3-.1l-6 3.8-2.6-.8c-.6-.2-.6-.6.1-.9z"/></svg>Telegram</span>
  <span class="chip"><svg viewBox="0 0 24 24"><path fill="#00AC47" d="M4 3h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-8l-5 4v-4H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/></svg>Google Chat</span>
  <span class="chip"><svg viewBox="0 0 24 24"><rect x="10" y="2" width="4" height="9" rx="2" fill="#36C5F0"/><rect x="13" y="10" width="9" height="4" rx="2" fill="#2EB67D"/><rect x="10" y="13" width="4" height="9" rx="2" fill="#ECB22E"/><rect x="2" y="10" width="9" height="4" rx="2" fill="#E01E5A"/></svg>Slack</span>
  <span class="chip"><svg viewBox="0 0 24 24"><defs><linearGradient id="msg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00B2FF"/><stop offset="1" stop-color="#0068FF"/></linearGradient></defs><path fill="url(#msg)" d="M12 2C6.2 2 2 6.4 2 12.1c0 3 1.3 5.6 3.4 7.3V23l3.2-1.8c.8.2 1.6.3 2.4.3 5.8 0 10-4.4 10-10.1S17.8 2 12 2z"/><path fill="#fff" d="M6.4 14.6l2.9-4.6 2.6 2 2.4-2.6-2.9 4.5-2.5-1.9z"/></svg>Messenger</span>
  <span class="chip"><svg viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#0068FF"/><path fill="#fff" d="M12 6.2c-3.2 0-5.8 2.1-5.8 4.8 0 1.5.8 2.9 2.1 3.8L7.7 17l2.5-1.3c.6.1 1.2.2 1.8.2 3.2 0 5.8-2.1 5.8-4.8S15.2 6.2 12 6.2z"/></svg>Zalo</span>
</div>

<p class="soon">Coming soon — <strong>Microsoft Teams · KakaoTalk · Naver Works</strong></p>

<!--
⏱ 6:15–7:00 — REACH
Broadcast: "Whatever your team lives in — one of these is almost certainly it."
Sweep across the logos. Call out KakaoTalk / Zalo if the room is KR / VN.
-->

---

<span class="eyebrow">Get started</span>

## Live in two minutes.

<div class="steps">
  <div class="step"><div class="b">1</div><div><h3>Connect your repo</h3><p>Authorise the secure GitHub App — code never leaves your repo.</p></div></div>
  <div class="step"><div class="b">2</div><div><h3>Invite Rio to your chat</h3><p>Personal or group, any channel.</p></div></div>
  <div class="step"><div class="b">3</div><div><h3>Send your first request — from your phone</h3><p>Type it. Tap approve. Watch it ship.</p></div></div>
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

<span class="eyebrow">🔴 Live demo</span>

## From a phone, in Google Chat.

<p class="muted">One message → a plan you approve → a preview link. Under a minute.</p>

</div>
<div>
  <div class="phone">
    <div class="screen">
      <div class="gc-head"><img src="assets/robot.svg"><div><div class="nm">Rio</div><div class="st">Active in Google Chat</div></div></div>
      <div class="gc-body">
        <div class="gc-day">Today</div>
        <div class="bub out">Make the “Sign up” button green and a bit bigger 🙏</div>
        <div class="bub in"><div class="who">Rio</div>Got it — CTA to brand green, larger. Here’s the plan — approve before I ship?</div>
        <div class="approve">⏸ Approve plan</div>
        <div class="bub out">ok, go ahead ✅</div>
        <div class="bub in"><div class="who">Rio</div>Done on <b>dev</b>, tests passing. Preview ready 🚀 — approve it?</div>
        <div class="approve">⏸ Approve preview</div>
        <div class="bub in"><div class="who">Rio</div>Approved. Sent to your manager to merge into <b>main</b>.</div>
        <div class="approve mgr">⏸ Approve merge · Manager</div>
        <div class="bub in"><div class="who">Rio</div>Merged to <b>main</b>. Live now 🎉</div>
      </div>
    </div>
  </div>
</div>
</div>

<script>
/* Replays the chat animation each time the demo slide becomes active.
   Marp scopes theme CSS under <section>, but bespoke's active class sits on the
   ancestor <svg> — unreachable from CSS. So we toggle .is-playing on .gc-body
   (inside the section) instead, which restarts the staggered CSS animation. */
(function(){
  function play(svg){
    var b = svg.querySelector('.gc-body'); if(!b) return;
    b.classList.remove('is-playing'); void b.offsetWidth; b.classList.add('is-playing');
  }
  function handle(svg){
    var on = svg.classList.contains('bespoke-marp-active');
    if(on && svg.querySelector('.gc-body') && !svg._rioOn){ svg._rioOn = 1; play(svg); }
    else if(!on){ svg._rioOn = 0; }
  }
  function init(){
    document.querySelectorAll('svg.bespoke-marp-slide').forEach(function(svg){
      new MutationObserver(function(){ handle(svg); })
        .observe(svg, { attributes:true, attributeFilter:['class'] });
      handle(svg);
    });
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else setTimeout(init, 0);
})();
</script>

<!--
⏱ 7:30–9:15 — LIVE DEMO (the finale, right before the ask)
Do it live if possible: real chat → plan → approve → preview link. Pre-load a
repo and a rehearsed change. If risky in a big webinar, play a screen recording
here instead. Narrate the two gates — then go straight to the closing ask.
-->

---

<!-- _class: close -->

# Hand maintenance to Rio.<br>Keep the decisions.

<p class="cta"><strong>Book a 20-minute setup</strong> — we’ll connect one repo and run a live change with you.</p>

<p class="url">https://rio.sotatek.kr</p>

<p class="thanks">Thank you for listening 🙏</p>

<!--
⏱ 9:15–10:00 — CLOSE WITH THE ASK
One clear next step for the whole room: "Drop your email / scan this — we'll
book 20 minutes to connect one repo and run a real change this week."
End on the ask, not "thank you". Then open Q&A.
-->
