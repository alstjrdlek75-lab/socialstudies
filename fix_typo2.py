with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = "공저거래위원회"
replacement = "공정거래위원회"

count = text.count(target)
print(f"Found {count} occurrences of {target}")

if count > 0:
    text = text.replace(target, replacement)
    with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully replaced typo in topics-data.js")
