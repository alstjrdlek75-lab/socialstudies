import re

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Since it's a JS file, we'll just isolate the array part
# Actually, I can just regex replace on the entire text since I know the exact pattern.
# But regex in python might fail if there's escaping.
# Let's try replacing exact block in python:

html_block = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(6) 고소·고발, 자수, 현행범체포 등에 의해 개시</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div><div class="group-content space-y-2 pl-1"></div></div>'
html_rename = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="6"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(7) 수사기관</span>  </div>'
html_rename_target = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(6) 수사기관</span>  </div>'

if html_block in text:
    text = text.replace(html_block, '')
    print("Block removed.")
else:
    # Maybe escaping in string? Let's use regex
    pattern = r'<div class=\\"topic-group mb-3\.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all\\" data-group-index=\\"5\\"><div class=\\"flex items-center justify-between border-b border-slate-100 pb-2\.5 mb-2\.5\\">  <div class=\\"font-bold text-sm md:text-base text-blue-700 flex items-center gap-2\\">    <span class=\\"w-2\.5 h-2\.5 rounded-full bg-blue-600 shrink-0\\"></span>    <span>\(6\) 고소·고발, 자수, 현행범체포 등에 의해 개시</span>.*?</div></div></div>'
    if re.search(pattern, text):
        text = re.sub(pattern, '', text)
        print("Block removed via regex.")
    else:
        print("Block still not found.")

pattern_rename = r'data-group-index=\\"6\\"(><div class=\\"flex items-center justify-between border-b border-slate-100 pb-2\.5 mb-2\.5\\">  <div class=\\"font-bold text-sm md:text-base text-blue-700 flex items-center gap-2\\">    <span class=\\"w-2\.5 h-2\.5 rounded-full bg-blue-600 shrink-0\\"></span>    <span>)\(7\) 수사기관(</span>)'
if re.search(pattern_rename, text):
    text = re.sub(pattern_rename, r'data-group-index=\"5\"\g<1>(6) 수사기관\g<2>', text)
    print("Renamed via regex.")
else:
    print("Rename pattern not found.")

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
    f.write(text)

