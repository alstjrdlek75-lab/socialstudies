path = '/Users/mac/.gemini/antigravity/scratch/edurecall/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

line = "localStorage.removeItem('edurecall_custom_SOC-151');"
if line not in content:
    content = content.replace(
        "localStorage.removeItem('edurecall_custom_SOC-147');",
        f"{line}\n        localStorage.removeItem('edurecall_custom_SOC-147');"
    )

import re
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
content = re.sub(
    r"explanations-data\.js\?v=[^\"]+",
    f"explanations-data.js?v={timestamp}",
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added SOC-151 cache invalidation and bumped version")
