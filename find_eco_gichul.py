import json

with open("topics-data.js", "r") as f:
    content = f.read()
start_idx = content.find("window.ALL_TOPICS = [") + len("window.ALL_TOPICS = ")
json_str = content[start_idx:].strip()
if json_str.endswith(";"): json_str = json_str[:-1]

topics = json.loads(json_str)

eco_keywords = ["경제", "미시", "거시", "시장", "국민소득", "화폐", "수요", "공급", "무역", "환율", "독점", "과점", "한계", "효용", "비용", "기회비용", "탄력성", "필립스", "실업", "인플레이션", "이자율", "투자", "GDP", "GNP", "외부효과", "공공재"]

eco_gichuls = []
for t in topics:
    if t.get("subject") == "기출":
        text = (t.get("title") + " " + t.get("contentHtml", "") + " " + t.get("defaultAnswer", "")).lower()
        
        # heuristic: if it mentions many economic terms, it's probably economics.
        # But wait! I can just use GPT to classify them, or maybe I can list all the titles and see.
        count = sum(1 for k in eco_keywords if k in text)
        if count >= 3:
            eco_gichuls.append(t)

print(f"Found {len(eco_gichuls)} potential economics questions.")
for t in eco_gichuls:
    print(f"[{t.get('id')}] {t.get('chapter')} - {t.get('title')}")
