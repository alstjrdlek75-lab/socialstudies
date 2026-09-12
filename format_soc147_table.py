import json
import re

path = '/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js'
with open(path, 'r', encoding='utf-8') as f:
    raw = f.read()

prefix = "window.ALL_TOPICS = "
suffix = ";"

assert raw.startswith(prefix)
clean_json = raw[len(prefix):].rstrip()
if clean_json.endswith(suffix):
    clean_json = clean_json[:-len(suffix)]

topics = json.loads(clean_json)

target = None
for t in topics:
    if t.get('id') == 'SOC-147':
        target = t
        break

if not target:
    print("SOC-147 not found!")
    exit(1)

# 1. Update defaultAnswer
old_ans_part = "(7) 신사회운동 [22 기출]\n①배경\n- 포디즘 → 포스트 포디즘\n- 산업사회 → 탈산업사회\n- 물질주의 → 탈물질주의 구사회운동(노동운동) 신사회운동 주체 노동자 다양한 계층(신중간 계급, 전문직, 자유 직 등) 이념 (가치)** 물질주의, 성장주의 탈물질주의, 탈권위주의, 풀뿌리 민주주의 쟁점 경제적 불평등 완화, 복지 환경, 여성, 장애, 인권, 평화 등 조직 수직적, 위계적 수평적 네트워크 운동 방식 관례적 인습적 비관례적"

new_ans_part = """(7) 신사회운동 [22 기출]
①배경
- 포디즘 → 포스트 포디즘
- 산업사회 → 탈산업사회
- 물질주의 → 탈물질주의
②구사회운동(노동운동)과 신사회운동 비교
- 주체: [구] 노동자 / [신] 다양한 계층(신중간 계급, 전문직, 자유직 등)
- 이념(가치): [구] 물질주의, 성장주의 / [신] 탈물질주의, 탈권위주의, 풀뿌리 민주주의
- 쟁점: [구] 경제적 불평등 완화, 복지 / [신] 환경, 여성, 장애, 인권, 평화 등
- 조직: [구] 수직적, 위계적 / [신] 수평적 네트워크
- 운동 방식: [구] 관례적, 인습적 / [신] 비관례적"""

assert old_ans_part in target['defaultAnswer'], "Could not find old answer part in defaultAnswer"
target['defaultAnswer'] = target['defaultAnswer'].replace(old_ans_part, new_ans_part)

# 2. Update contentHtml for Group 7 (data-group-index="6")
table_html = """<div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">①배경</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 포디즘 → 포스트 포디즘</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 산업사회 → 탈산업사회</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 물질주의 → <span class="mask-tape" data-tape="true" data-text="탈물질주의">탈물질주의</span></div><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all mt-2.5">②구사회운동(노동운동)과 신사회운동 비교</div><div class="overflow-x-auto my-2.5"><table class="w-full border-collapse border border-slate-200 text-center text-xs md:text-sm"><thead><tr class="bg-slate-50 font-semibold text-slate-700"><th class="border border-slate-200 p-2 bg-slate-100/80 w-1/5">구분</th><th class="border border-slate-200 p-2 text-blue-800 bg-blue-50/50 w-2/5">구사회운동(노동운동)</th><th class="border border-slate-200 p-2 text-indigo-800 bg-indigo-50/50 w-2/5">신사회운동</th></tr></thead><tbody><tr><th class="border border-slate-200 p-2 bg-slate-50 font-semibold text-slate-700">주체</th><td class="border border-slate-200 p-2 text-slate-700"><span class="mask-tape" data-tape="true" data-text="노동자">노동자</span></td><td class="border border-slate-200 p-2 text-slate-700">다양한 계층(<span class="mask-tape" data-tape="true" data-text="신중간 계급">신중간 계급</span>, 전문직, 자유직 등)</td></tr><tr><th class="border border-slate-200 p-2 bg-slate-50 font-semibold text-slate-700">이념(가치)</th><td class="border border-slate-200 p-2 text-slate-700"><span class="mask-tape" data-tape="true" data-text="물질주의">물질주의</span>, 성장주의</td><td class="border border-slate-200 p-2 text-slate-700"><span class="mask-tape" data-tape="true" data-text="탈물질주의">탈물질주의</span>, 탈권위주의, 풀뿌리 민주주의</td></tr><tr><th class="border border-slate-200 p-2 bg-slate-50 font-semibold text-slate-700">쟁점</th><td class="border border-slate-200 p-2 text-slate-700">경제적 불평등 완화, 복지</td><td class="border border-slate-200 p-2 text-slate-700">환경, 여성, 장애, 인권, 평화 등</td></tr><tr><th class="border border-slate-200 p-2 bg-slate-50 font-semibold text-slate-700">조직</th><td class="border border-slate-200 p-2 text-slate-700"><span class="mask-tape" data-tape="true" data-text="수직적, 위계적">수직적, 위계적</span></td><td class="border border-slate-200 p-2 text-slate-700"><span class="mask-tape" data-tape="true" data-text="수평적 네트워크">수평적 네트워크</span></td></tr><tr><th class="border border-slate-200 p-2 bg-slate-50 font-semibold text-slate-700">운동 방식</th><td class="border border-slate-200 p-2 text-slate-700">관례적, 인습적</td><td class="border border-slate-200 p-2 text-slate-700"><span class="mask-tape" data-tape="true" data-text="비관례적">비관례적</span></td></tr></tbody></table></div>"""

old_g7_pattern = r'(data-group-index="6"><div class="flex items-center justify-between border-b border-slate-100 pb-2\.5 mb-2\.5">.*?<div class="group-content space-y-2 pl-1">)(.*?)</div></div>$'
match = re.search(old_g7_pattern, target['contentHtml'], re.DOTALL)
assert match, "Could not match group 6 content in contentHtml"

target['contentHtml'] = target['contentHtml'][:match.start(2)] + table_html + "</div></div>"

# Count tapeCount
tapes = re.findall(r'class="mask-tape"', target['contentHtml'])
target['tapeCount'] = len(tapes)

# Add new target keywords if not present
new_kws = ["탈물질주의", "신중간 계급", "수평적 네트워크", "비관례적"]
for kw in new_kws:
    if kw not in target['targetKeywords']:
        target['targetKeywords'].append(kw)

print(f"Updated tapeCount: {target['tapeCount']}")

# Save back to file
new_raw = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + suffix + "\n"
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_raw)

print("Successfully updated SOC-147 table format!")
