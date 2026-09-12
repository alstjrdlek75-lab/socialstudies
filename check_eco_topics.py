import json
with open("topics-data.js", "r") as f:
    content = f.read()
start_idx = content.find("window.ALL_TOPICS = [") + len("window.ALL_TOPICS = ")
json_str = content[start_idx:].strip()
if json_str.endswith(";"): json_str = json_str[:-1]

topics = json.loads(json_str)
eco_topics = [t for t in topics if t.get("subject") == "경제학"]
for t in eco_topics:
    print(f"[{t.get('id')}] {t.get('chapter')} - {t.get('section')} - {t.get('title')}")
