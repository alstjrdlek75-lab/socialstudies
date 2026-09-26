# Edurecall Project Rules & Execution Guidelines

This file defines the mandatory operational constraints and pair programming behaviors for the Antigravity assistant working on the Edurecall codebase.

---

## 1. Tool Loop Prohibition & Action Threshold (무한 조회 및 분석 마비 원천 차단)

* **Maximum 2 Reads per Region (동일 영역 조회 제한)**:
  * Never call `view_file` on the same file range or closely overlapping lines more than twice within a single turn.
  * If the issue location or root cause has been identified, **stop reading immediately** and transition directly to writing code (`replace_file_content` / `write_to_file`) or running commands.
* **No Endless Internal Loops (무출력 도구 루프 금지)**:
  * Do not run more than 5 consecutive tool calls without either producing visible textual output to the user or completing an actionable step.
  * Avoid theoretical overthinking: apply the change and let the compiler, syntax checker, or browser verify the result.

---

## 2. Decisive Action & Fail-Fast Verification (과감한 실행 및 자동 검증)

* **Git-Backed Confidence**:
  * Every file is tracked under Git version control. Never hesitate to modify code out of fear of breaking things; unexpected issues can be reverted cleanly in seconds via `git checkout`.
* **Automated Verification Over Imagination**:
  * After editing `topics-data.js`: verify syntax immediately with `node -c topics-data.js`.
  * After editing `index.html`: verify visually when needed with headless Chrome screenshots or remote debugging.
* **Atomic Step Execution**:
  * For multi-faceted tasks (e.g., data content + editor parser + localStorage migration):
    1. Apply the core data/markup update first.
    2. Apply parser/editor safeguards.
    3. Add storage cleanup / migration logic.
    4. Test and verify.
    5. Commit, push, and deploy to Vercel.

---

## 3. Edurecall Quality & Design System Standards

* **Table Standards**:
  * Always use modern responsive table markup matching `POL-108` and `LAW-041`:
    * Outer container: `mt-1 overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800 shadow-2xs`
    * Table element: `w-full text-xs md:text-sm text-center border-collapse`
    * Thead: `bg-slate-100/90 dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-bold border-b border-slate-200 dark:border-slate-700`
    * Header cells: distinctive color accents (`bg-blue-50/70`, `bg-rose-50/70`, `bg-emerald-50/70` with matching dark mode styles)
    * Tbody rows: `divide-y divide-slate-200 dark:divide-slate-800 bg-white dark:bg-slate-900` with subtle hover effects and bold label column.
* **Card Editor Integrity**:
  * Never strip or flatten `<table>` elements into single-line plaintext. Always preserve table wrappers (`rawTableHtml`) during card parsing and serialization.
* **Storage Cache Safeguards**:
  * When changing core topic structures that might have been cached in user browsers under `edurecall_custom_<topicId>`, always provide an automated purge or version migration (`edurecall_migration_vX_done`) to prevent corrupted overrides.

---

## 4. Deployment Protocol

* After making and verifying changes, always execute:
  1. `git add -A && git commit -m "..."`
  2. `git push origin main`
  3. `npx vercel --prod --yes`
* Ensure the live production site ([https://edurecall.vercel.app](https://edurecall.vercel.app)) is updated cleanly.
