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
        if sum(1 for k in eco_keywords if k in text) >= 3:
            # exclude sociology / politics
            if not any(k in text for k in ["하버마스", "권위", "왈츠", "레짐", "바·바스", "혹실드", "고프먼"]):
                eco_gichuls.append(t)

print(f"Filtered to {len(eco_gichuls)} true economics questions.")

chapters = [
    "1. 미시경제학", "2. 거시경제학", "3. 국제경제학"
]
sections = {
    "1. 미시경제학": [
        "1-1. 경제학 일반론", "1-2. 소비자이론", "1-3. 생산자이론", "1-4. 수요·공급이론", "1-5. 시장이론", "1-6. 분배이론", "1-7. 시장실패"
    ],
    "2. 거시경제학": [
        "2-1. 국민소득측정", "2-2. 소비투자이론", "2-3. 국민소득결정", "2-4. 화폐금융론", "2-5. 거시균형이론", "2-6. 물가와실업", "2-7. 경제성장론"
    ],
    "3. 국제경제학": [
        "3-1. 국제무역론", "3-2. 환율과국제수지", "3-3. 개방거시균형"
    ]
}

def classify(title, content):
    text = title + " " + content
    if "무역" in text or "비교우위" in text or "관세" in text or "수입할당" in text:
        return "3. 국제경제학", "3-1. 국제무역론"
    if "환율" in text or "국제수지" in text or "구매력평가" in text:
        return "3. 국제경제학", "3-2. 환율과국제수지"
    if "스완" in text or "먼델" in text or "개방경제" in text:
        return "3. 국제경제학", "3-3. 개방거시균형"
    if "국민소득" in text or "총수요" in text or "총공급" in text or "승수" in text or "디플레이션" in text or "인플레이션" in text or "투자" in text or "유동성" in text or "통화정책" in text:
        if "총수요-총공급" in text or "인플레이션 갭" in text:
            return "2. 거시경제학", "2-5. 거시균형이론"
        if "유동성" in text or "통화정책" in text:
            return "2. 거시경제학", "2-4. 화폐금융론"
        if "승수" in text or "폐쇄 거시경제" in text:
            return "2. 거시경제학", "2-3. 국민소득결정"
        if "현재가치" in text or "소비" in text:
            return "2. 거시경제학", "2-2. 소비투자이론"
        return "2. 거시경제학", "2-5. 거시균형이론"
    if "수요독점" in text or "임금" in text or "노동공급" in text or "여가" in text:
        return "1. 미시경제학", "1-6. 분배이론"
    if "시장실패" in text or "외부효과" in text or "공공재" in text or "피구세" in text or "배출권" in text or "코즈" in text:
        return "1. 미시경제학", "1-7. 시장실패"
    if "독점" in text or "과점" in text or "완전경쟁" in text:
        return "1. 미시경제학", "1-5. 시장이론"
    if "탄력성" in text or "가격효과" in text or "가격상한제" in text or "가격지지" in text or "조세" in text or "자중손실" in text or "잉여" in text:
        return "1. 미시경제학", "1-4. 수요·공급이론"
    if "생산함수" in text or "등비용" in text or "이윤극대화" in text:
        return "1. 미시경제학", "1-3. 생산자이론"
    if "한계효용" in text or "무차별" in text or "소비자 균형" in text or "대체효과" in text or "소득효과" in text:
        return "1. 미시경제학", "1-2. 소비자이론"
    if "기회비용" in text or "매몰비용" in text:
        return "1. 미시경제학", "1-1. 경제학 일반론"
    return "1. 미시경제학", "1-4. 수요·공급이론"

# Create new duplicated items
new_items = []
for t in eco_gichuls:
    new_t = t.copy()
    new_t["subject"] = "경제학"
    chap, sec = classify(new_t["title"], new_t["contentHtml"])
    new_t["chapter"] = chap
    new_t["section"] = sec
    # Prefix title with original exam year so users know it's a past exam!
    # original chapter is "2014학년도 기출"
    year_prefix = t["chapter"].split(" ")[0] # "2014학년도"
    # the title is something like "5번. [기입5] ..."
    new_t["title"] = f"[{year_prefix}] {t['title']}"
    new_items.append(new_t)

# Insert the new items right after the original economics ones, or at the end.
# Actually, appending at the end is easiest.
topics.extend(new_items)

# Write back
with open("topics-data.js", "w") as f:
    f.write("window.ALL_TOPICS = ")
    f.write(json.dumps(topics, indent=2, ensure_ascii=False))
    f.write(";")
print(f"Added {len(new_items)} items to '경제학'.")
