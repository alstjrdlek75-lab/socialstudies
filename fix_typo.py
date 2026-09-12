with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = "체포·구속 ㄹ적부심사"
replacement = "체포·구속 적부심사"

if target in text:
    text = text.replace(target, replacement)
    with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully replaced typo in topics-data.js")
else:
    print("Target not found")
