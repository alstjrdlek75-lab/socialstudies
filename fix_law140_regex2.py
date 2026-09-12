import re

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update contentHtml
# Let's just find the exact text using simple string replace
import urllib.parse
html_block_to_remove = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(6) 고소·고발, 자수, 현행범체포 등에 의해 개시</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div><div class="group-content space-y-2 pl-1"></div></div>'
if html_block_to_remove in text:
    text = text.replace(html_block_to_remove, '')
    print("HTML block removed")

# 2. Rename (7) 수사기관 to (6)
html_rename_from = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="6"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(7) 수사기관</span>  </div>'
html_rename_to = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(6) 수사기관</span>  </div>'
if html_rename_from in text:
    text = text.replace(html_rename_from, html_rename_to)
    print("HTML renamed")

# 3. Update answer
ans_remove = "(6) 고소·고발, 자수, 현행범체포 등에 의해 개시\\n\\n(7) 수사기관: 검사, 사법경찰관"
ans_replace = "(6) 수사기관: 검사, 사법경찰관"
if ans_remove in text:
    text = text.replace(ans_remove, ans_replace)
    print("Ans replaced")

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
    f.write(text)

