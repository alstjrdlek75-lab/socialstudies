import re
from datetime import datetime

path = '/Users/mac/.gemini/antigravity/scratch/edurecall/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update explanations-data.js version
timestamp = datetime.now().strftime('%Y%m%d_%H%M')
content = re.sub(
    r'explanations-data\.js\?v=\d+_\d+',
    f'explanations-data.js?v={timestamp}',
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Bumped version to", timestamp)
