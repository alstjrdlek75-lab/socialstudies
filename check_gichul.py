import json

with open("topics-data.js", "r") as f:
    content = f.read()
    
# Extract the JSON array part
start_idx = content.find("window.ALL_TOPICS = [") + len("window.ALL_TOPICS = ")
json_str = content[start_idx:]
# It might end with a semicolon, but json.loads needs valid json
json_str = json_str.strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

try:
    topics = json.loads(json_str)
    gichul = [t for t in topics if t.get("subject") == "기출"]
    print(f"Total topics: {len(topics)}")
    print(f"Total in '기출': {len(gichul)}")
    
    # What are the chapters/sections in '기출'?
    from collections import Counter
    print(Counter([t.get("chapter") for t in gichul]))
except Exception as e:
    print(f"Error parsing JSON: {e}")
