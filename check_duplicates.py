import json

path = '/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js'
with open(path, 'r', encoding='utf-8') as f:
    raw = f.read()[len("window.ALL_TOPICS = "):].rstrip()[:-1]
    topics = json.loads(raw)

ids_to_check = [
    "POL-014", "POL-032", # 토의민주주의
    "POL-027", "POL-034", # 자유주의
    "POL-031", "POL-035", # 공화주의 / 공동체주의
    "POL-054", "POL-056"  # 다원주의 국가론
]

for t in topics:
    if t["id"] in ids_to_check:
        print(f"=== {t['id']} {t['title']} ===")
        print(t["defaultAnswer"].strip())
        print()
