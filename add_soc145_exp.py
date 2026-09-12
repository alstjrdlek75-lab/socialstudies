import re
import json

path = '/Users/mac/.gemini/antigravity/scratch/edurecall/explanations-data.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure window.TOPIC_EXPLANATIONS exists and is a JS object
match = re.search(r'window\.TOPIC_EXPLANATIONS\s*=\s*(\{.*?\});', content, re.DOTALL)
if not match:
    print("Could not find window.TOPIC_EXPLANATIONS")
    exit(1)

explanations = json.loads(match.group(1))

explanations["SOC-145"] = {
    "title": "종속적 발전론 (Dependent Development)",
    "background": "<b>등장 배경: 종속이론의 한계 극복</b><br>초기 종속이론(프랑크)은 '주변부 국가가 중심부 국가와 관계를 맺으면 구조적 착취로 인해 발전이 불가능하고 저발전이 심화된다(저발전의 발전)'고 주장했습니다. 그러나 1970년대 브라질이나 한국 등 신흥 공업국(NICs)들이 중심부 국가에 경제적으로 의존하면서도 <b>고도의 산업화와 경제성장</b>을 이룩하는 현상이 나타났습니다. <b>카르도소(Cardoso)</b>와 <b>에반스(Evans)</b>는 이러한 현실을 설명하기 위해 <b>종속적 발전론</b>을 제시했습니다.",
    "analogyTitle": "핵심 개념: 3자 연합(Triple Alliance)과 국가의 역할",
    "analogy": "1. <b>3자 연합 (Triple Alliance)</b><br>에반스는 신흥 공업국의 발전이 <b>외국 자본(다국적 기업)</b>, <b>국가(정부)</b>, <b>국내 자본(토착 기업)</b> 간의 긴밀한 연합을 통해 이루어진다고 보았습니다. 외국 자본은 기술과 자본을 제공하고, 국내 자본은 값싼 노동력과 생산 기반을 제공하며, 국가는 이 둘을 매개하고 지원하는 역할을 합니다.<br><br>2. <b>국가의 적극적 역할 (내부 요인의 강조)</b><br>단순히 외부에서 착취당하는 수동적인 상태가 아니라, <b>강력한 국가(발전국가)</b>가 주도적으로 경제 계획을 세우고 다국적 기업과 협상하며 국내 자본을 육성하는 등 <b>내부적 요인(국가의 자율성과 역량)</b>이 발전의 핵심 축으로 작용합니다.<br><br>3. <b>'종속적' 발전의 한계</b><br>경제 성장은 일어나지만, 핵심 기술이나 막대한 자본, 주요 수출 시장을 여전히 중심부에 의존해야 하므로 <b>구조적 종속은 계속 유지</b>됩니다. 또한, 성장 위주의 정책으로 인해 국내의 빈부격차나 노동 착취 등 불평등이 심화되는 부작용도 수반됩니다.",
    "subnoteBridge": "<b>서브노트 본문 연결 포인트:</b><br>• <b>외국 자본-국가-국내 자본의 연합:</b> 에반스의 '3자 연합' 개념을 지칭합니다. 여기서 <b>국가의 적극적인 역할</b>이 매개체로서 매우 중요합니다.<br>• <b>종속적 발전 가능:</b> 종속이론과 달리, 종속된 상태에서도 <b>산업화와 경제 성장(발전)이 가능함</b>을 인정합니다.<br>• <b>내부적 요인 고려:</b> 기존 종속이론이 외부적(국제적) 착취 구조에만 집착했던 것과 달리, 개별 국가 내부의 정치·계급 구조, 정부의 정책 역량 등 <b>내부적 요인</b>을 함께 분석한다는 점이 가장 큰 차별점입니다."
}

updated_json = json.dumps(explanations, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + updated_json + content[match.end(1):]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected SOC-145 explanation!")
