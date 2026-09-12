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
            import re
            
            # 1. Remove (6) block
            html = t['contentHtml']
            html = re.sub(r'<div class="topic-group[^>]*data-group-index="5".*?\(6\) 고소·고발, 자수, 현행범체포 등에 의해 개시.*?</div></div></div>', '', html)
            
            # 2. Rename (7) 수사기관 to (6) 수사기관 and data-group-index="6" to "5"
            html = re.sub(r'data-group-index="6"(>.*?<span>)\(7\) 수사기관(</span>)', r'data-group-index="5"\g<1>(6) 수사기관\g<2>', html)
            t['contentHtml'] = html
            
            # Fix defaultAnswer
            ans = t['defaultAnswer']
            ans = re.sub(r'\(6\) 고소·고발, 자수, 현행범체포 등에 의해 개시\n\n\(7\) 수사기관', r'(6) 수사기관', ans)
            t['defaultAnswer'] = ans
            
            # Fix groupCount
            t['groupCount'] = 6
            
            print("LAW-140 fixed.")
            break
            
    # Write back, formatting exactly to match style (though indent=2 might change slightly if the original was indent=2)
    # Actually, original is 2 spaces.
    out_text = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + ";\n"
    with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
        f.write(out_text)
    print("Done")
else:
    print("Prefix not found.")
