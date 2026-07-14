---
marp: true
theme: rio
title: Rio — AI 유지보수 엔지니어 (KO)
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
    <div class="brand-row"><span class="brand">Rio</span><span class="eyebrow">AI 유지보수 엔지니어</span></div>
    <h1>한 번의 메시지.<br><em>소프트웨어가 배포됩니다.</em></h1>
  </div>
</div>

<p class="sub"><strong>당신이 자는 동안</strong> 코드베이스를 유지보수하는 AI 엔지니어 — 모두 휴대폰에서. 변경을 입력하고 <strong>승인만 하면</strong> Rio가 배포합니다.</p>

<p class="url">https://rio.sotatek.kr</p>

<!--
⏱ 0:00–0:45 — TITLE / HOOK
"Imagine fixing your live product by sending one chat message — and still
approving everything before it goes out. That's Rio."
Let people settle. One strong sentence, then move on.
-->

---

<span class="eyebrow">익숙한 문제</span>

## 일주일을 기다린 사소한 수정.

<p class="muted">아이디어가 부족한 게 아니라, ‘사소하지만 급한’ 일을 맡을 여유 있는 엔지니어 팀이 없을 뿐입니다.</p>

<div class="stats">
  <div class="stat"><div class="k">3–7일</div><p>한 줄 수정에 걸리는 시간.</p></div>
  <div class="stat"><div class="k">“잠깐이면 돼…”</div><p>티켓과 회의 속에 파묻힘.</p></div>
  <div class="stat"><div class="k">통제 불가</div><p>AI가 알아서 배포하는 것에 대해.</p></div>
</div>

<!--
⏱ 0:45–2:00 — THE PAIN
Broadcast poll: "Show of hands / yes in chat — who has a one-line change stuck
in a queue right now?" Wait 3 seconds, acknowledge, move on. The nods sell it.
-->

---

<div class="cols">
<div>

<span class="eyebrow">Rio 소개</span>

## 당신이 주도하는 AI 팀원.

- **쉬운 말**로 변경을 설명 — 티켓도, 전문 용어도 없이
- **당신의 저장소에서 바로** 작업 (안전한 GitHub App)
- 모든 배포는 **사람의 승인 관문**을 통과
- **24/7** — 자정에 보내면 아침엔 검토할 변경이 준비

> 자율적으로 일하고, 사람이 통제합니다.

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

<span class="eyebrow">작동 방식 — 두 관문은 당신 몫</span>

## 다섯 단계는 자동. 두 단계는 당신.

<div class="flow">
  <div class="node"><div class="dot">1</div><div class="lb">요청 보내기</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">2</div><div class="lb">Rio가 분석</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">3</div><div class="lb">계획 승인</div><div class="who">⏸ 최종 사용자</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">4</div><div class="lb">dev에서 코딩</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">5</div><div class="lb">테스트 + 미리보기</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">6</div><div class="lb">미리보기 승인</div><div class="who">⏸ 최종 사용자</div></div>
  <div class="arrow">→</div>
  <div class="node gate"><div class="dot">7</div><div class="lb">병합 승인</div><div class="who">⏸ 관리자</div></div>
  <div class="arrow">→</div>
  <div class="node"><div class="dot">8</div><div class="lb">배포 + 보고</div></div>
</div>

<!--
⏱ 3:00–4:30 — THE FLOW
Don't narrate all 7. "Five are automatic. Two are yours" — point at 3 and 6.
That contrast is the whole story.
-->

---

<span class="eyebrow">세 관문 = 당신의 통제권</span>

## Rio는 절대 무단으로 배포하지 않습니다.

<div class="gates">
  <div class="gatecard">
    <div class="g">⏸ 관문 1 · 최종 사용자</div>
    <h3>최종 사용자가 계획을 승인</h3>
    <p>Rio가 한 줄이라도 쓰기 전에 최종 사용자가 <em>무엇을</em> <em>왜</em> 하는지 봅니다. “ok”라고 답하거나 수정합니다.</p>
  </div>
  <div class="gatecard">
    <div class="g">⏸ 관문 2 · 최종 사용자</div>
    <h3>최종 사용자가 미리보기를 승인</h3>
    <p>Rio는 먼저 <code>dev</code>에 배포합니다. 최종 사용자가 미리보기 링크를 열어 맞는지 확인한 뒤 다음 단계로 넘어갑니다.</p>
  </div>
  <div class="gatecard">
    <div class="g">⏸ 관문 3 · 관리자</div>
    <h3>관리자가 병합을 승인</h3>
    <p>권한 있는 사람만 마지막 버튼을 누릅니다. 그 외 누구도 <code>main</code>을 건드리지 않습니다.</p>
  </div>
</div>

<!--
⏱ 4:30–5:15 — TRUST (objection-killer)
This slide disarms the #1 fear: "AI touching our live code." Say the headline
slowly and literally. Pause. Then move into why teams trust it.
-->

---

<span class="eyebrow">팀이 Rio를 신뢰하는 이유</span>

## 제멋대로인 봇이 아닙니다.

<div class="tiles">
  <div class="tile g"><div class="ic">⏸</div><h3>세 승인 관문</h3><p>계획 + 미리보기 + 병합, 생략 없음.</p></div>
  <div class="tile"><div class="ic">◇</div><h3>당신의 저장소</h3><p>안전한 GitHub App — 코드는 벗어나지 않음.</p></div>
  <div class="tile"><div class="ic">◷</div><h3>24/7, 대기 없음</h3><p>티켓도 회의도 없음.</p></div>
  <div class="tile"><div class="ic">⌥</div><h3>안전한 dev 브랜치</h3><p>운영 전에 테스트 & 미리보기.</p></div>
  <div class="tile"><div class="ic">✎</div><h3>당신의 언어</h3><p>쉬운 말로 입력, 비즈니스 용어로 보고 — EN · VI · KO.</p></div>
  <div class="tile"><div class="ic">◱</div><h3>멀티테넌트</h3><p>고객마다 격리된 전용 공간.</p></div>
</div>

<!--
⏱ 5:15–6:15 — WHY TRUST
Mixed audience → SPEAK ONLY the top row (two gates · your own repo · 24/7).
One sentence for the rest: "…plus your dev branch, your language, full tenant
isolation." Let the slide carry them.
-->

---

<span class="eyebrow">멀티채널</span>

## 이미 쓰는 채팅 앱 그대로.

<p class="muted">새 도구도, 새 습관도 없이. 1:1이든 그룹이든 — 스레드 하나 = 요청 하나.</p>

<div class="chips">
  <span class="chip"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#29A9EA"/><path fill="#fff" d="M5.5 11.7l11.2-4.3c.5-.2 1 .1.8.9l-1.9 9c-.1.5-.5.7-.9.4l-2.6-1.9-1.3 1.2c-.1.1-.3.2-.5.2l.2-2.7 4.9-4.4c.2-.2 0-.3-.3-.1l-6 3.8-2.6-.8c-.6-.2-.6-.6.1-.9z"/></svg>Telegram</span>
  <span class="chip"><svg viewBox="0 0 24 24"><path fill="#00AC47" d="M4 3h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-8l-5 4v-4H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/></svg>Google Chat</span>
  <span class="chip"><svg viewBox="0 0 24 24"><rect x="10" y="2" width="4" height="9" rx="2" fill="#36C5F0"/><rect x="13" y="10" width="9" height="4" rx="2" fill="#2EB67D"/><rect x="10" y="13" width="4" height="9" rx="2" fill="#ECB22E"/><rect x="2" y="10" width="9" height="4" rx="2" fill="#E01E5A"/></svg>Slack</span>
  <span class="chip"><svg viewBox="0 0 24 24"><defs><linearGradient id="msg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00B2FF"/><stop offset="1" stop-color="#0068FF"/></linearGradient></defs><path fill="url(#msg)" d="M12 2C6.2 2 2 6.4 2 12.1c0 3 1.3 5.6 3.4 7.3V23l3.2-1.8c.8.2 1.6.3 2.4.3 5.8 0 10-4.4 10-10.1S17.8 2 12 2z"/><path fill="#fff" d="M6.4 14.6l2.9-4.6 2.6 2 2.4-2.6-2.9 4.5-2.5-1.9z"/></svg>Messenger</span>
  <span class="chip"><svg viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#0068FF"/><path fill="#fff" d="M12 6.2c-3.2 0-5.8 2.1-5.8 4.8 0 1.5.8 2.9 2.1 3.8L7.7 17l2.5-1.3c.6.1 1.2.2 1.8.2 3.2 0 5.8-2.1 5.8-4.8S15.2 6.2 12 6.2z"/></svg>Zalo</span>
</div>

<p class="soon">곧 지원 — <strong>Microsoft Teams · KakaoTalk · Naver Works</strong></p>

<!--
⏱ 6:15–7:00 — REACH
Broadcast: "Whatever your team lives in — one of these is almost certainly it."
Sweep across the logos. Call out KakaoTalk / Zalo if the room is KR / VN.
-->

---

<span class="eyebrow">시작하기</span>

## 2분이면 시작.

<div class="steps">
  <div class="step"><div class="b">1</div><div><h3>저장소 연결</h3><p>안전한 GitHub App 승인 — 코드는 저장소를 벗어나지 않아요.</p></div></div>
  <div class="step"><div class="b">2</div><div><h3>채팅에 Rio 초대</h3><p>1:1이든 그룹이든, 어떤 채널이든.</p></div></div>
  <div class="step"><div class="b">3</div><div><h3>첫 요청 보내기 — 휴대폰에서</h3><p>입력하고. 승인 탭하고. 배포 확인.</p></div></div>
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

<span class="eyebrow">🔴 라이브 데모</span>

## 휴대폰에서, Google Chat으로.

<p class="muted">메시지 하나 → 승인할 계획 → 미리보기 링크. 1분 이내.</p>

</div>
<div>
  <div class="phone">
    <div class="screen">
      <div class="gc-head"><img src="assets/robot.svg"><div><div class="nm">Rio</div><div class="st">Google Chat에서 활성</div></div></div>
      <div class="gc-body">
        <div class="gc-day">오늘</div>
        <div class="bub out">‘가입’ 버튼을 초록색으로, 조금 더 크게 해줘 🙏</div>
        <div class="bub in"><div class="who">Rio</div>알겠어요 — CTA를 브랜드 초록색으로, 더 크게. 계획입니다 — 배포 전에 승인해 주실래요?</div>
        <div class="approve">⏸ 계획 승인</div>
        <div class="bub out">네, 진행하세요 ✅</div>
        <div class="bub in"><div class="who">Rio</div><b>dev</b>에 완료, 테스트 통과. 미리보기 준비됐어요 🚀 — 승인해 주실래요?</div>
        <div class="approve">⏸ 미리보기 승인</div>
        <div class="bub in"><div class="who">Rio</div>승인됨. <b>main</b> 병합을 위해 관리자에게 보냈어요.</div>
        <div class="approve mgr">⏸ 병합 승인 · 관리자</div>
        <div class="bub in"><div class="who">Rio</div><b>main</b>에 병합. 라이브 됐어요 🎉</div>
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

# 유지보수는 Rio에게.<br>결정은 당신이.

<p class="cta"><strong>20분 설정 미팅 예약</strong> — 저장소 하나를 연결해 실제 변경을 함께 실행합니다.</p>

<p class="url">https://rio.sotatek.kr</p>

<p class="thanks">경청해 주셔서 감사합니다 🙏</p>

<!--
⏱ 9:15–10:00 — CLOSE WITH THE ASK
One clear next step for the whole room: "Drop your email / scan this — we'll
book 20 minutes to connect one repo and run a real change this week."
End on the ask, not "thank you". Then open Q&A.
-->
