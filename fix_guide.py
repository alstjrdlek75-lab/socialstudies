import re
import json

with open('topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Isolate GUIDE-001
parts = text.split('"id": "GUIDE-001"')
if len(parts) != 2:
    print("Could not find GUIDE-001 block")
    exit(1)

pre = parts[0]
post = '"id": "GUIDE-001"' + parts[1]

# split up to EXAM-2026-A-01
subparts = post.split('"id": "EXAM-2026-A-01"')
block = subparts[0]
rest = '"id": "EXAM-2026-A-01"' + subparts[1]

# 1. Update defaultAnswer
old_ans = """(5) F / A / P 평가 (회독 및 취약점 관리)
① 서술 연습 후 본인의 암기 완성도에 따라 F(Fail, 미인출/오답), A(Again, 불완전), P(Pass, 완벽인출) 버튼을 눌러 상태를 기록합니다. (단축키: 1 / 2 / 3)
② 평가 결과는 좌측 목차에 색상으로 반영되며, 다음 N회독 집중 복습 시 취약한 주제를 우선적으로 정복하는 데 활용하십시오."""

new_ans = """(5) FSRS 알고리즘 기반 복습 평가 (최적의 장기기억 형성)
① 서술 연습 후 본인의 인출 완성도에 따라 1(다시), 2(어려움), 3(알맞음), 4(쉬움) 버튼을 눌러 상태를 기록합니다. (단축키: 1 / 2 / 3 / 4)
② FSRS(뇌과학 기반 간격 반복 알고리즘)가 최적의 다음 복습일을 자동으로 계산해 줍니다.
③ 사이트 메인의 [🗓️ 오늘 복습] 탭에서 알고리즘이 오늘 꼭 복습해야 한다고 알려주는 카드(Due)만 모아서 효율적으로 정복하십시오."""

block = block.replace(old_ans, new_ans)

old_ans_shortcut = "- 1, 2, 3 : 각각 자가진단 평가 F, A, P 기록"
new_ans_shortcut = "- 1, 2, 3, 4 : 각각 1(다시), 2(어려움), 3(알맞음), 4(쉬움) 기록"
block = block.replace(old_ans_shortcut, new_ans_shortcut)

# 2. Update contentHtml
old_html_1 = """<span>(5) F / A / P 평가 (회독 및 취약점 관리)</span></div></div><div class=\\"group-content space-y-2 pl-1\\"><div class=\\"recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all\\">① 서술 연습 후 본인의 암기 완성도에 따라 <span class=\\"font-bold text-red-600\\">F(Fail, 미인출/오답)</span>, <span class=\\"font-bold text-amber-500\\">A(Again, 불완전)</span>, <span class=\\"font-bold text-emerald-600\\">P(Pass, 완벽인출)</span> 버튼을 눌러 상태를 기록합니다. (단축키: <span class=\\"font-bold\\">1 / 2 / 3</span>)</div><div class=\\"recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all\\">② 평가 결과는 좌측 목차에 색상으로 반영되며, 다음 <span class=\\"mask-tape\\" data-tape=\\"true\\" data-text=\\"N회독 집중 복습\\">N회독 집중 복습</span> 시 취약한 주제를 우선적으로 정복하는 데 활용하십시오.</div></div></div>"""

new_html_1 = """<span>(5) FSRS 알고리즘 기반 복습 평가 (최적의 장기기억 형성)</span></div></div><div class=\\"group-content space-y-2 pl-1\\"><div class=\\"recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all\\">① 서술 연습 후 본인의 인출 완성도에 따라 <span class=\\"font-bold text-red-500\\">1(다시)</span>, <span class=\\"font-bold text-amber-500\\">2(어려움)</span>, <span class=\\"font-bold text-emerald-500\\">3(알맞음)</span>, <span class=\\"font-bold text-blue-500\\">4(쉬움)</span> 버튼을 눌러 상태를 기록합니다. (단축키: <span class=\\"font-bold\\">1 / 2 / 3 / 4</span>)</div><div class=\\"recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all\\">② FSRS(뇌과학 기반 간격 반복 알고리즘)가 최적의 다음 복습일을 자동으로 계산해 줍니다.</div><div class=\\"recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all\\">③ 사이트 메인의 <strong>[🗓️ 오늘 복습]</strong> 탭에서 알고리즘이 <span class=\\"mask-tape\\" data-tape=\\"true\\" data-text=\\"오늘 꼭 복습해야 한다고 알려주는 카드(Due)\\">오늘 꼭 복습해야 한다고 알려주는 카드(Due)</span>만 모아서 효율적으로 정복하십시오.</div></div></div>"""

if old_html_1 not in block:
    print("old_html_1 not found!")
else:
    block = block.replace(old_html_1, new_html_1)

old_html_shortcut = """<br/>- <span class=\\"font-bold\\">1, 2, 3</span> : 각각 자가진단 평가 F, A, P 기록<br/>"""
new_html_shortcut = """<br/>- <span class=\\"font-bold\\">1, 2, 3, 4</span> : 각각 1(다시), 2(어려움), 3(알맞음), 4(쉬움) 기록<br/>"""

if old_html_shortcut not in block:
    print("old_html_shortcut not found!")
else:
    block = block.replace(old_html_shortcut, new_html_shortcut)

# 3. Update keywords
block = block.replace('"N회독 집중 복습"', '"오늘 꼭 복습해야 한다고 알려주는 카드(Due)"')

new_text = pre + block + rest

with open('topics-data.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully updated GUIDE-001 in topics-data.js")
