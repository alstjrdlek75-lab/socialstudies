import json

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read().strip()

prefix = "window.ALL_TOPICS = "
json_data = text[len(prefix):]
if json_data.endswith(';'):
    json_data = json_data[:-1]

topics = json.loads(json_data)

# 1. Remove age classification lines from LAW-171 (3. 단체행동권과 쟁의행위)
law171 = next(t for t in topics if t['id'] == 'LAW-171')

html_to_remove = """<div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 17세: 미성년자(O), 연소근로자(O)</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 18세: 미성년자(O), 연소근로자(X)</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 19세: 성년(미성년자X), 연소근로자(X)</div>"""
law171['contentHtml'] = law171['contentHtml'].replace(html_to_remove, "")

ans_to_remove = """- 17세: 미성년자(O), 연소근로자(O)\n- 18세: 미성년자(O), 연소근로자(X)\n- 19세: 성년(미성년자X), 연소근로자(X)\n"""
law171['defaultAnswer'] = law171['defaultAnswer'].replace(ans_to_remove, "")

# 2. Add age classification lines into LAW-163 (5. 연소자 근로의 특별보호)
# Specifically in (2) 연소근로자 정의:
law163 = next(t for t in topics if t['id'] == 'LAW-163')

old_group1 = """<span>(2) 연소근로자 정의</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div><div class="group-content space-y-2 pl-1"><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">15세 이상 18세 미만인 자</div></div></div>"""

new_group1 = """<span>(2) 연소근로자 정의 및 미성년자와의 구별</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div><div class="group-content space-y-2 pl-1"><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">15세 이상 18세 미만인 자</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 17세: 미성년자(O), 연소근로자(O)</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 18세: 미성년자(O), 연소근로자(X)</div><div class="recall-item text-xs md:text-sm text-slate-600 leading-relaxed pl-6 py-0.5 transition-all">- 19세: 성년(미성년자X), 연소근로자(X)</div></div></div>"""

law163['contentHtml'] = law163['contentHtml'].replace(old_group1, new_group1)

old_ans_group1 = "(2) 연소근로자 정의: 15세 이상 18세 미만인 미성년자"
new_ans_group1 = """(2) 연소근로자 정의: 15세 이상 18세 미만인 자
- 17세: 미성년자(O), 연소근로자(O)
- 18세: 미성년자(O), 연소근로자(X)
- 19세: 성년(미성년자X), 연소근로자(X)"""

law163['defaultAnswer'] = law163['defaultAnswer'].replace(old_ans_group1, new_ans_group1)

out_text = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + ";\n"
with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
    f.write(out_text)

print("Done moving age classification from LAW-171 to LAW-163.")
