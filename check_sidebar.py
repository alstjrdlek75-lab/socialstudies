import re

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check how sidebar renders numbers
print("Has formatTitle or similar:", "formatTitle" in text)
