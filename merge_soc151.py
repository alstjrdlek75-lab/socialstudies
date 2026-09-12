import json

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
    if t.get('id') == 'SOC-151':
        target = t
        break

if not target:
    print("SOC-151 not found!")
    exit(1)

# Update defaultAnswer
target['defaultAnswer'] = """4. 하버마스의 공론장과 체계-생활세계이론
(1) 주요내용
①체계: 사적인 영역의 경제체계(시장경제)와 공적 영역의 행정체계
- 목적 합리성과 효율성의 원리에 의해 작동
②생활세계: 의사소통적 합리성 발달에 따라 친밀성의 영역(사적)과 공적 공론장으로 분화
- 의사소통적 합리성의 원리에 의해 작동
③문예적 공론장 – 정치적 공론장 – 의회민주주의로 제도화
④정치적 공론장의 재봉건화: 의회로 제도화되었지만, 전문적 기술관료에 의해 공론장 쇠퇴
⑤생활세계의 식민화 [25 기출]: 체계의 화폐 논리와 권력 논리가 의사소통적 합리성을 억압
+국가가 제공하는 사회복지 또는 사회보장
"""

# Update contentHtml
target['contentHtml'] = """<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="0"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(1) 주요내용</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div><div class="group-content space-y-2 pl-1"><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">①체계: 사적인 영역의 경제체계(시장경제)와 공적 영역의 행정체계</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 목적 합리성과 효율성의 원리에 의해 작동</div><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">②생활세계: <span class="mask-tape" data-tape="true" data-text="의사소통적 합리성">의사소통적 합리성</span> 발달에 따라 친밀성의 영역(사적)과 <span class="mask-tape" data-tape="true" data-text="공적 공론장">공적 공론장</span>으로 분화</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 의사소통적 합리성의 원리에 의해 작동</div><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">③문예적 공론장 – 정치적 공론장 – 의회민주주의로 제도화</div><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">④정치적 공론장의 재봉건화: 의회로 제도화되었지만, 전문적 기술관료에 의해 공론장 쇠퇴</div><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">⑤생활세계의 식민화 <span class="exam-badge">25 기출</span>: 체계의 <span class="mask-tape" data-tape="true" data-text="화폐">화폐</span> 논리와 <span class="mask-tape" data-tape="true" data-text="권력">권력</span> 논리가 의사소통적 합리성을 억압</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">+국가가 제공하는 사회복지 또는 사회보장</div></div></div>"""

new_raw = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + suffix + "\n"
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_raw)

print("Successfully merged SOC-151 content!")
