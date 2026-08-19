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
  <img src="assets/robot.svg" alt="Rio" style="width:200px;height:200px;border-radius:44px;box-shadow:0 0 70px 8px rgba(34,197,94,.4)">
</div>
</div>

<!--
⏱ 2:00–3:00 — POSITIONING
Land the frame BEFORE the mechanics: not "an AI that codes" — "an AI teammate
that maintains your product, with you in charge." Say the tagline out loud.
-->

---

<span class="eyebrow">How it works — three human gates</span>

## Rio runs the flow. Three gates need a human.

<div class="flow">
  <div class="node"><div class="dot">1</div><div class="lb">Send request</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">2</div><div class="lb">Rio analyses</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">3</div><div class="lb">Approve plan</div><div class="who">⏸ END USER</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">4</div><div class="lb">Code on dev</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">5</div><div class="lb">Test + preview</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">6</div><div class="lb">Approve preview</div><div class="who">⏸ END USER</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">7</div><div class="lb">Approve merge</div><div class="who">⏸ MANAGER</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">8</div><div class="lb">Ship + report</div></div>
</div>

<div class="gates">
  <div class="gatecard">
    <div class="g">⏸ GATE 1 · END USER</div>
    <h3>End user approves the plan</h3>
    <p>Before Rio writes a single line, the end user sees <em>what</em> it will do and <em>why</em> — and replies “ok”, or refines it.</p>