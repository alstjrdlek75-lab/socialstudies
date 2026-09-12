import json

with open("topics-data.js", "r") as f:
    content = f.read()
    
start_idx = content.find("window.ALL_TOPICS = [") + len("window.ALL_TOPICS = ")
json_str = content[start_idx:].strip()
if json_str.endswith(";"): json_str = json_str[:-1]

try:
    topics = json.loads(json_str)
    from collections import Counter
    print(Counter([t.get("subject") for t in topics]))
except Exception as e:
    print(f"Error parsing JSON: {e}")
