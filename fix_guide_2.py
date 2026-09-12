import re
import json

with open('topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('"id": "GUIDE-001"')
if len(parts) != 2:
    print("Could not find GUIDE-001 block")
    exit(1)

pre = parts[0]
post = '"id": "GUIDE-001"' + parts[1]

subparts = post.split('"id": "EXAM-2026-A-01"')
block = subparts[0]
rest = '"id": "EXAM-2026-A-01"' + subparts[1]

# 1. Update defaultAnswer
old_ans = "(5) F / A / P 평가 (회독 및 취약점 관리)\\n① 서술 연습 후 본인의 암기 완성도에 따라 F(Fail, 미인출/오답), A(Again, 불완전), P(Pass, 완벽인출) 버튼을 눌러 상태를 기록합니다. (단축키: 1 / 2 / 3)\\n② 평가 결과는 좌측 목차에 색상으로 반영되며, 다음 N회독 집중 복습 시 취약한 주제를 우선적으로 정복하는 데 활용하십시오."

new_ans = "(5) FSRS 알고리즘 기반 복습 평가 (최적의 장기기억 형성)\\n① 서술 연습 후 본인의 인출 완성도에 따라 1(다시), 2(어려움), 3(알맞음), 4(쉬움) 버튼을 눌러 상태를 기록합니다. (단축키: 1 / 2 / 3 / 4)\\n② FSRS(뇌과학 기반 간격 반복 알고리즘)가 최적의 다음 복습일을 자동으로 계산해 줍니다.\\n③ 사이트 메인의 [🗓️ 오늘 복습] 탭에서 알고리즘이 오늘 꼭 복습해야 한다고 알려주는 카드(Due)만 모아서 효율적으로 정복하십시오."

if old_ans not in block:
    print("old_ans not found!")
else:
    block = block.replace(old_ans, new_ans)

new_text = pre + block + rest

with open('topics-data.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully updated GUIDE-001 defaultAnswer in topics-data.js")
