import json

log_file = "/Users/mac/.gemini/antigravity/brain/4a70d882-2b4c-4198-8306-012686530f35/.system_generated/logs/transcript_full.jsonl"
with open(log_file, "r") as f:
    lines = f.readlines()

for idx, line in enumerate(reversed(lines)):
    try:
        data = json.loads(line)
        if data.get("type") == "USER_INPUT":
            content = data.get("content", "")
            print(f"USER INPUT {idx}: {content[:100]}...")
    except:
        pass
