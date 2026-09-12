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
        if t['id'] == 'LAW-146':
            import re
            
            # 1. Update (3) 방어권 고지 to merge the text into ①변호인의 조력을 받을 권리
            # Old item: ①변호인의 조력을 받을 권리
            # New item: ①변호인의 조력을 받을 권리: 수사, 공판 단계 수사기관과 대등한 관계에서 방어
            t['contentHtml'] = t['contentHtml'].replace(
                '①변호인의 조력을 받을 권리</div>',
                '①변호인의 조력을 받을 권리: 수사, 공판 단계 수사기관과 대등한 관계에서 방어</div>'
            )
            
            # 2. Remove group (4) 변호인의 조력을 받을 권리 completely
            # Find and remove the group container for index 3
            group4_pattern = r'<div class="topic-group mb-3\.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="3">.*?<span>\(4\) 변호인의 조력을 받을 권리</span>.*?</div></div></div>'
            t['contentHtml'] = re.sub(group4_pattern, '', t['contentHtml'])
            
            # 3. Update defaultAnswer
            old_ans = "(3) 방어권 고지\n①변호인의 조력을 받을 권리\n②진술거부권: 자기부죄 거부의 특권에서 유래, 피의자 피고인 모두 해당\n(4) 변호인의 조력을 받을 권리: 수사, 공판 단계 수사기관과 대등한 관계에서 방어"
            new_ans = "(3) 방어권 고지\n①변호인의 조력을 받을 권리: 수사, 공판 단계 수사기관과 대등한 관계에서 방어\n②진술거부권: 자기부죄 거부의 특권에서 유래, 피의자 피고인 모두 해당"
            t['defaultAnswer'] = t['defaultAnswer'].replace(old_ans, new_ans)
            
            # 4. Update groupCount
            t['groupCount'] = 3
            
            print("LAW-146 successfully updated.")
            break
            
    out_text = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + ";\n"
    with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
        f.write(out_text)
    print("Done writing to topics-data.js")
else:
    print("Prefix not found.")
