import json

path = '/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js'
with open(path, 'r', encoding='utf-8') as f:
    raw = f.read()

prefix = "window.ALL_TOPICS = "
suffix = ";"

assert raw.startswith(prefix)
clean_json = raw[len(prefix):].rstrip()
if clean_json.endswith(suffix):
    clean_json = clean_json[:-len(suffix)]

topics = json.loads(clean_json)

target = None
for t in topics:
    if t.get('id') == 'SOC-146':
        target = t
        break

if not target:
    print("SOC-146 not found!")
    exit(1)

print("Original defaultAnswer:")
print(target['defaultAnswer'])

# 1. Update defaultAnswer
# remove (4) 비교 and any trailing newlines
target['defaultAnswer'] = target['defaultAnswer'].replace("(4) 비교\n", "").rstrip() + "\n"

# 2. Update contentHtml: remove data-group-index="3" which contains (4) 비교
import re
target['contentHtml'] = re.sub(
    r'<div class="topic-group[^"]*" data-group-index="3">.*?</div></div>',
    '',
    target['contentHtml'],
    flags=re.DOTALL
)

print("\nUpdated defaultAnswer:")
print(target['defaultAnswer'])

# Save back to file
new_raw = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + suffix + "\n"
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_raw)

print("Successfully updated SOC-146 in topics-data.js!")
