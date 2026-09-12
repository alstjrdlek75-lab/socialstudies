import re

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update contentHtml
# Find the exact (6) block and remove it
pattern_html = r'<div class="topic-group mb-3\.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="5">.*?<span>\(6\) 고소·고발, 자수, 현행범체포 등에 의해 개시</span>.*?</div></div></div>'
text = re.sub(pattern_html, '', text)

# Now rename (7) to (6) and update data-group-index="6" to "5"
pattern_rename = r'data-group-index="6"(>.*?<span>)\(7\) 수사기관(</span>)'
text = re.sub(pattern_rename, r'data-group-index="5"\g<1>(6) 수사기관\g<2>', text)

# 2. Update defaultAnswer
pattern_ans = r'\(6\) 고소·고발, 자수, 현행범체포 등에 의해 개시\n\n\(7\) 수사기관'
text = re.sub(pattern_ans, r'(6) 수사기관', text)

# 3. Update groupCount for LAW-140
# We need to target the block for LAW-140 only.
# It ends with:
#     "tapeCount": 0,
#     "groupCount": 7
#   },
#   {
#     "id": "LAW-141",
pattern_gc = r'"tapeCount": 0,\n    "groupCount": 7\n  \},\n  \{\n    "id": "LAW-141"'
text = re.sub(pattern_gc, r'"tapeCount": 0,\n    "groupCount": 6\n  },\n  {\n    "id": "LAW-141"', text)

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
    f.write(text)

