import json

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read().strip()

prefix = "window.ALL_TOPICS = "
json_data = text[len(prefix):]
if json_data.endswith(';'):
    json_data = json_data[:-1]

topics = json.loads(json_data)

for t in topics:
    if t['id'] == 'SOC-144':
        t['title'] = "3. 세계체계 이론"
        t['defaultAnswer'] = t['defaultAnswer'].replace("3. 사회체계 이론", "3. 세계체계 이론")
        print("Updated SOC-144 title and defaultAnswer.")
        break

out_text = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + ";\n"
with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
    f.write(out_text)

print("Done.")
