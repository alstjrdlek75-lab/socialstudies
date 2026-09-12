import json

with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'r', encoding='utf-8') as f:
    text = f.read().strip()

prefix = "window.ALL_TOPICS = "
json_data = text[len(prefix):]
if json_data.endswith(';'):
    json_data = json_data[:-1]

topics = json.loads(json_data)

# 1. Merge content of LAW-163 into LAW-163 with full protection rules:
law163 = next(t for t in topics if t['id'] == 'LAW-163')

# We want 6 groups in LAW-163:
# Group 0: (1) 최저취업연령 및 예외
#          15세 미만인 자(중학교 재학 중인 18세 미만 포함)는 원칙적으로 근로자로 사용 불가 (단, 고용노동부장관의 취직인허증 소지 시 가능)
# Group 1: (2) 연소근로자 정의
#          15세 이상 18세 미만인 자
# Group 2: (3) 근로계약
#          법정대리인의 동의를 받아 본인이 직접 체결 → 법정대리인이 미성년자의 근로계약을 대리할 수 없음
# Group 3: (4) 법정근로시간
#          1일 7시간, 1주 35시간 / 합의 시 1일 1시간, 1주 5시간까지 연장 가능
# Group 4: (5) 야간·휴일근로
#          원칙적 금지, 단 본인의 동의와 고용노동부 장관의 인가 시 가능
# Group 5: (6) 독자적 임금 청구권
#          미성년자는 독자적으로 임금을 청구할 수 있음 (법정대리인이 대신 수령 불가)

def make_group(idx, title, content=""):
    content_div = f'<div class="group-content space-y-2 pl-1"><div class="recall-item text-sm md:text-[15px] text-slate-800 leading-relaxed pl-3.5 border-l-2 border-blue-200 py-1 transition-all">{content}</div></div>' if content else '<div class="group-content space-y-2 pl-1"></div>'
    return f'<div class="topic-group mb-3.5 bg-white border border-slate-200 rounded-xl p-4 shadow-2xs transition-all" data-group-index="{idx}"><div class="flex items-center justify-between border-b border-slate-100 pb-2.5 mb-2.5">  <div class="font-bold text-sm md:text-base text-blue-700 flex items-center gap-2">    <span class="w-2.5 h-2.5 rounded-full bg-blue-600 shrink-0"></span>    <span>{title}</span>  </div>  <button class="group-toggle-btn text-xs text-slate-400 hover:text-slate-700 px-2 py-0.5 rounded hover:bg-slate-100 flex items-center gap-1" type="button" title="이 항목 블러 토글">    <span class="material-symbols-outlined text-[16px]">visibility</span>  </button></div>{content_div}</div>'

groups_html = [
    make_group(0, "(1) 최저취업연령 (아동 노동 금지)", "15세 미만인 자(중학교에 재학 중인 18세 미만 포함)는 원칙적으로 근로자로 사용 불가, 취직인허증을 발급받은 경우 예외적으로 취업 가능"),
    make_group(1, "(2) 연소근로자 정의", "15세 이상 18세 미만인 자"),
    make_group(2, "(3) 근로계약 체결", "법정대리인의 동의를 받아 본인이 직접 체결 → 법정대리인이 미성년자의 근로계약을 대리할 수 없음 (친권자나 후견인은 미성년자의 근로계약을 대리할 수 없음)"),
    make_group(3, "(4) 법정근로시간", "1일 7시간, 1주 35시간 한도 / 당사자 간 합의 시 1일 1시간, 1주 5시간까지 연장 가능 (주 최대 40시간)"),
    make_group(4, "(5) 야간·휴일근로 제한", "원칙적 금지, 단 본인의 동의와 고용노동부 장관의 인가를 받은 경우 예외적으로 가능 (18세 미만자 및 산후 1년 미만 여성)"),
    make_group(5, "(6) 독자적 임금 청구", "미성년자는 독자적으로 임금을 청구할 수 있음 (법정대리인이 임금을 대신 수령할 수 없음)")
]

law163['contentHtml'] = "".join(groups_html)
law163['groupCount'] = 6
law163['defaultAnswer'] = """5. 연소근로자의 특별보호
(1) 최저취업연령: 15세 미만인 자(중학교 재학 중인 18세 미만 포함)는 원칙적으로 고용 불가, 취직인허증 소지 시 예외적 허용
(2) 연소근로자 정의: 15세 이상 18세 미만인 미성년자
(3) 근로계약 체결: 법정대리인의 동의를 받아 본인이 직접 체결 (대리 체결 금지)
(4) 법정근로시간: 1일 7시간, 1주 35시간 / 합의 시 1일 1시간, 1주 5시간 연장 한도
(5) 야간·휴일근로: 원칙적 금지, 본인 동의 + 고용노동부 장관의 인가 시 예외적 허용
(6) 독자적 임금 청구: 미성년자가 독자적으로 임금 청구 가능 (대리 수령 금지)
"""

law163['targetKeywords'] = list(set(law163.get('targetKeywords', []) + [
    "취직인허증", "15세", "18세", "법정대리인", "대리", "7시간", "35시간", "인가", "임금", "연소근로자"
]))

# 2. Remove LAW-167 from topics
topics = [t for t in topics if t['id'] != 'LAW-167']

# 3. Renumber titles in this section after LAW-163
# Previous numbering:
# LAW-163: 5. 연소자 근로의 특별보호
# LAW-164: 6. 근로감독관 제도의 권한
# LAW-165: 7. 해고의 제한 및 구제신청
# LAW-166: 8. 최저임금제도의 효력
# (LAW-167 removed)
# LAW-168: 10. 이행강제금 제도 -> should become "9. 이행강제금 제도"

for t in topics:
    if t['id'] == 'LAW-168':
        t['title'] = t['title'].replace("10. ", "9. ")

out_text = prefix + json.dumps(topics, ensure_ascii=False, indent=2) + ";\n"
with open('/Users/mac/.gemini/antigravity/scratch/edurecall/topics-data.js', 'w', encoding='utf-8') as f:
    f.write(out_text)

print(f"Merge completed. Total topics count: {len(topics)}")
