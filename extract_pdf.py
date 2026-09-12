import json
import re

log_file = "/Users/mac/.gemini/antigravity/brain/4a70d882-2b4c-4198-8306-012686530f35/.system_generated/logs/transcript_full.jsonl"
with open(log_file, "r") as f:
    lines = f.readlines()

pdf_text = ""
for line in reversed(lines):
    try:
        data = json.loads(line)
        if data.get("type") == "USER_INPUT":
            content = data.get("content", "")
            if "<Start of PDF>" in content and "<End of PDF>" in content:
                start = content.find("<Start of PDF>")
                end = content.find("<End of PDF>") + len("<End of PDF>")
                pdf_text = content[start:end]
                break
    except:
        pass

if pdf_text:
    with open("pdf_text.txt", "w") as f:
        f.write(pdf_text)
    print("Extracted PDF text to pdf_text.txt")
else:
    print("Could not find PDF text")
