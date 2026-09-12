import json

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read().strip()

prefix = "window.ALL_TOPICS = "
if text.startswith(prefix):
    json_data = text[len(prefix):]
    if json_data.endswith(';'):
        json_data = json_data[:-1]
    
    topics = json.loads(json_data)
    
    for t in topics:
        if t['id'] == 'LAW-140':
            # Append the (6) 수사기관 block to contentHtml
            susagigwan_block = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(6) 수사기관</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div><div class="group-content space-y-2 pl-1"><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">검사, 사법경찰관</div></div></div>'
            t['contentHtml'] += susagigwan_block
            
            print("LAW-140 restored 수사기관 block.")
            break
            
    out_text = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + ";\n"
    with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
        f.write(out_text)
    print("Done")
