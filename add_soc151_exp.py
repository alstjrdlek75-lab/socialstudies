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

explanations["SOC-151"] = {
    "title": "하버마스의 공론장과 체계-생활세계 이론 (25 기출)",
    "background": "<b>등장 배경: 현대 사회의 병리 현상 진단</b><br>하버마스는 현대 사회를 물질적 재생산을 담당하는 <b>'체계(System)'</b>와 상징적 재생산(의미, 규범, 정체성 형성)을 담당하는 <b>'생활세계(Lifeworld)'</b>의 이원적 구조로 파악했습니다. 그는 근대화의 성과를 인정하면서도, 자본주의와 관료제가 팽창하면서 인간의 고유한 삶의 터전인 생활세계를 파괴하는 병리 현상을 비판했습니다.",
    "analogyTitle": "핵심 개념: 체계 vs 생활세계, 그리고 식민화",
    "analogy": "1. <b>체계(System) vs 생활세계(Lifeworld)의 구분</b><br>• <b>체계:</b> 사적 영역인 <b>경제(시장)</b>와 공적 영역인 <b>행정(국가)</b>으로 구성됩니다. 이 영역은 언어가 아니라 <b>'화폐'</b>와 <b>'권력'</b>이라는 조종 매체에 의해 움직이며, <b>도구적·목적 합리성(효율성)</b>이 지배합니다.<br>• <b>생활세계:</b> 가족 등 사적 영역(친밀성)과 시민들의 <b>공적 공론장</b>으로 구성됩니다. 강제나 계산이 아닌 언어를 통한 대화와 <b>의사소통적 합리성(상호 이해와 합의)</b>의 원리로 작동합니다.<br><br>2. <b>정치적 공론장의 재봉건화 (Refeudalization)</b><br>초기 부르주아 시민들은 살롱과 카페(문예적 공론장)에서 출발하여 국가 권력을 비판하는 '정치적 공론장'을 형성하고 이를 의회민주주의로 제도화했습니다. 그러나 후기 자본주의로 오면서 <b>거대 매체의 상업화와 전문 기술관료(전문가 집단)</b>가 정책 결정을 독점하면서, 비판적 토론의 장이 사라지고 시민들은 수동적 소비자로 전락했습니다(중세 봉건 귀족의 일방적 권력 행사 시대로 되돌아간 것과 같다는 의미).<br><br>3. <b>생활세계의 식민화 (Colonization of the Lifeworld - [25 기출])</b><br>체계의 조종 매체인 <b>'화폐'</b>와 <b>'권력'</b>의 논리가 본래 의사소통적 합리성에 의해 유지되어야 할 가족, 학교, 문화, 시민사회 등 생활세계 깊숙이 침투하여 삶의 의미와 인간관계를 파괴하는 현상입니다.<br>• <i>예시:</i> 교육·의료 등 인간적 돌봄 영역이 수익 창출 수단으로 변질되거나(화폐 논리), 시민의 자율적 문제 해결 영역이 복지국가의 과도한 관료제적 법제화와 통제에 종속되는 현상(권력 논리).",
    "subnoteBridge": "<b>서브노트 인출 포인트 (2025학년도 기출 쟁점):</b><br>• <b>체계 작동 원리 및 매체:</b> 목적 합리성, 효율성 / 조종 매체: <b>화폐(경제), 권력(행정)</b><br>• <b>생활세계 작동 원리:</b> <b>의사소통적 합리성</b> (친밀성 영역 + <b>공적 공론장</b>)<br>• <b>정치적 공론장의 재봉건화:</b> 의회 제도화 이후 전문 기술관료와 상업주의에 의한 공론장 쇠퇴<br>• <b>생활세계의 식민화:</b> 체계의 <b>화폐와 권력</b> 논리가 생활세계로 침투하여 <b>의사소통적 합리성을 억압·파괴</b>하는 현상"
}

updated_json = json.dumps(explanations, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + updated_json + content[match.end(1):]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected SOC-151 explanation!")
