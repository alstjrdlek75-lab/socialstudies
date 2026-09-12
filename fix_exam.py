import re
import json

with open('topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('"id": "EXAM-2026-B-03"')
if len(parts) != 2:
    print("Could not find exactly one EXAM-2026-B-03 block.")
    exit(1)

pre = parts[0]
post = '"id": "EXAM-2026-B-03"' + parts[1]

subparts = post.split('"id": "EXAM-2026-B-04"')
block = subparts[0]
rest = '"id": "EXAM-2026-B-04"' + subparts[1]

block = block.replace('대주제화(대단원화, 대주제 통합)', '대강화(대단원화, 대강화 통합)')
block = block.replace('대주제화', '대강화')

block = block.replace('교육과정 연구자(연구자/개발자/생산자/반성적 실천가)', '교육과정 이론가(이론가/개발자/생산자/반성적 실천가)')
block = block.replace('교육과정 연구자', '교육과정 이론가')

block = block.replace('3) 연구자/개발자(Researcher/Developer)', '3) 이론가/개발자(Theorist/Developer)')
block = block.replace('반성적 연구자로서', '반성적 실천가로서')

new_text = pre + block + rest

with open('topics-data.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully updated topics-data.js")

