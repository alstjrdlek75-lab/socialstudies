path = '/Users/mac/.gemini/antigravity/scratch/edurecall/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

line = "localStorage.removeItem('edurecall_custom_SOC-146');"
if line not in content:
    content = content.replace(
        "localStorage.removeItem('edurecall_custom_SOC-145');",
        f"{line}\n        localStorage.removeItem('edurecall_custom_SOC-145');"
    )

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added SOC-146 cache invalidation")
