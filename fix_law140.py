import re

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update contentHtml
target_html_old = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(6) 고소·고발, 자수, 현행범체포 등에 의해 개시</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div><div class="group-content space-y-2 pl-1"></div></div><div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="6"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(7) 수사기관</span>  </div>'

target_html_new = '<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>(6) 수사기관</span>  </div>'

if target_html_old in text:
    text = text.replace(target_html_old, target_html_new)
    print("contentHtml fixed")
else:
    print("contentHtml NOT FOUND")

# 2. Update defaultAnswer
target_answer_old = """(5) 피의자: 수사 시작 후 참고인은 수사를 받는 자로 변경

(6) 고소·고발, 자수, 현행범체포 등에 의해 개시

(7) 수사기관: 검사, 사법경찰관"""

target_answer_new = """(5) 피의자: 수사 시작 후 참고인은 수사를 받는 자로 변경

(6) 수사기관: 검사, 사법경찰관"""

if target_answer_old in text:
    text = text.replace(target_answer_old, target_answer_new)
    print("defaultAnswer fixed")
else:
    print("defaultAnswer NOT FOUND")

# 3. Update groupCount for LAW-140
old_group_count = """    ],
    "tapeCount": 0,
    "groupCount": 7
  },
  {
    "id": "LAW-141","""

new_group_count = """    ],
    "tapeCount": 0,
    "groupCount": 6
  },
  {
    "id": "LAW-141","""

if old_group_count in text:
    text = text.replace(old_group_count, new_group_count)
    print("groupCount fixed")
else:
    print("groupCount NOT FOUND")

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
    f.write(text)

