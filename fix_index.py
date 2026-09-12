import re

path = '/Users/mac/.gemini/antigravity/scratch/edurecall/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add SOC-145 cache clearing
cache_lines = [
    "localStorage.removeItem('edurecall_custom_SOC-145');"
]

for line in cache_lines:
    if line not in content:
        content = content.replace(
            "// Migrate legacy LAW-045/LAW-046 entries to LAW-044",
            f"{line}\n        // Migrate legacy LAW-045/LAW-046 entries to LAW-044"
        )

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html cache clear rules")
