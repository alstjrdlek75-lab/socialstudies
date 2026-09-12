import json

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read().strip()

prefix = "window.ALL_TOPICS = "
json_data = text[len(prefix):]
if json_data.endswith(';'):
    json_data = json_data[:-1]

topics = json.loads(json_data)

law163 = next(t for t in topics if t['id'] == 'LAW-163')
law167 = next(t for t in topics if t['id'] == 'LAW-167')

print("=== LAW-163 contentHtml ===")
print(law163['contentHtml'])
print("=== LAW-163 defaultAnswer ===")
print(law163['defaultAnswer'])

print("=== LAW-167 contentHtml ===")
print(law167['contentHtml'])
print("=== LAW-167 defaultAnswer ===")
print(law167['defaultAnswer'])
