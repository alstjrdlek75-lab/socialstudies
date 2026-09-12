import re
import json

path = '/Users/mac/.gemini/antigravity/scratch/edurecall/explanations-data.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.TOPIC_EXPLANATIONS\s*=\s*(\{.*?\});', content, re.DOTALL)
if not match:
    print("Could not find window.TOPIC_EXPLANATIONS")
    exit(1)

explanations = json.loads(match.group(1))

explanations["SOC-147"] = {
    "title": "집합행동 및 초기 사회운동 4대 핵심 이론",
    "background": "<b>이론의 발전 흐름과 관점 차이</b><br>초기 집합행동 이론(르봉, 블루머)은 대중의 비이성적·감정적 충동에 주목하였고, 데이비스의 J-곡선 이론은 심리적 요인인 <b>'상대적 박탈감'</b>에 초점을 맞췄습니다. 반면 올슨의 합리적 선택이론은 참가자를 감정적 군중이 아닌 철저히 <b>비용과 편익을 따지는 이성적 존재</b>로 바라보며 무임승차자 문제를 제기했습니다.",
    "analogyTitle": "요청하신 4대 이론 핵심 포인트 요약",
    "analogy": "1. <b>군중심리 이론 (르봉)</b><br>• 군중에 속하면 개인의 이성과 자제력이 마비되고 원초적인 <b>집합심성</b>에 지배당합니다.<br>• <b>3가지 발현 기제:</b> <b>익명성</b>(개인 책임감 상실) → <b>전염</b>(타인의 감정·행동을 무비판적으로 모방) → <b>피암시성</b>(최면 상태처럼 선동가의 암시에 쉽게 굴복).<br><br>2. <b>순환반응 이론 (블루머)</b><br>• 자극에 이성적으로 해석하여 반응하는 것이 아니라, 서로의 감정이 피드백되어 증폭되는 비이성적 상호작용입니다.<br>• <b>4단계 과정:</b> <b>사회적 불안</b>(불안·동요) → <b>순환반응</b>(서로의 흥분을 반사적으로 주고받음) → <b>집합적 흥분</b>(자제력 완전 상실) → <b>사회적 전염</b>(주변으로 급속히 번져 군중행동 폭발).<br><br>3. <b>사회심리학적 혁명이론 (데이비스의 J-곡선 이론)</b><br>• 혁명은 가장 궁핍할 때 일어나는 것이 아니라, <b>'기대 수준'과 '실제 수준'의 격차가 참을 수 없을 만큼 벌어질 때(상대적 박탈감)</b> 발생합니다.<br>• 지속적 경제 발전으로 사람들의 기대치(J-곡선의 완만한 상승곡선)가 높아진 상태에서, 급격한 경기 침체로 현실 보상이 꺾일 때 폭발합니다.<br><br>4. <b>합리적 선택 이론 (올슨)</b><br>• 집합행동 참여자는 감정적인 군중이 아니라 <b>자기이익(비용 대비 편익)을 극대화하려는 합리적 행위자</b>입니다.<br>• <b>무임승차자 문제:</b> 사회운동이 추구하는 공공재(사회복지, 민주주의 등)는 비배제성을 띠므로, '내가 참여 비용(시간·돈·위험)을 치르지 않아도 남들이 성공하면 혜택을 누릴 수 있다'고 판단하여 무임승차하려는 모순(개인 합리성과 집단 합리성의 충돌)이 발생합니다.",
    "subnoteBridge": "<b>서브노트 인출 포인트 요약:</b><br>• <b>르봉:</b> 집합심성, 3대 기제(익명성, 전염, 피암시성)<br>• <b>블루머:</b> 순환반응 4단계 (사회적 불안 → 순환반응 → 집합적 흥분 → 사회적 전염)<br>• <b>데이비스:</b> J-곡선, 기대와 현실의 괴리, 상대적 박탈감<br>• <b>올슨:</b> 합리성, 개인과 집단의 합리성 모순, 무임승차자 문제"
}

updated_json = json.dumps(explanations, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + updated_json + content[match.end(1):]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected SOC-147 explanation!")
