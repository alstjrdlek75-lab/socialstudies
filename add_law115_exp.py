import json

with open('explanations-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# We want to insert the LAW-115 block safely into window.TOPIC_EXPLANATIONS.
# The easiest way is to find "window.TOPIC_EXPLANATIONS = {" and insert right after it.

insert_text = """
  "LAW-115": {
    "title": "7. 범죄의 처벌조건 및 처벌조각사유",
    "question": "범죄가 이미 성립했는데 왜 처벌을 안 하거나 면제해주는 조건이 별도로 존재할까요?",
    "analogyTitle": "처벌조건과 처벌조각사유의 법적 취지와 구별",
    "background": "어떤 행위가 구성요건에 해당하고, 위법하며, 책임이 인정되면 '범죄'가 성립합니다. 하지만 국가가 언제나 형벌권을 행사하는 것은 아닙니다. 형사정책적 고려나 다른 법익과의 형량을 위해, 범죄는 성립하지만 예외적으로 처벌을 유보하거나 면제하는 요건을 두는 경우가 있습니다.\\n\\n이러한 요건 중 범죄 성립 외부에서 객관적으로 요구되는 요건을 '객관적 처벌조건', 행위자의 특수한 신분 때문에 처음부터 형벌권이 배제되는 사유를 '인적 처벌조각사유'라고 부릅니다. 이는 범죄 성립 자체를 부정하는 '위법성조각사유'나 '책임조각사유'와는 구별되는 형법상의 독특한 개념입니다.",
    "analogy": "📌 범죄성립요건 vs 처벌요건\\n\\n① 객관적 처벌조건\\n- **의의**: 범죄 성립 후 형벌권 발생을 위해 범죄 행위와 무관하게 외부적으로 요구되는 객관적 사실\\n- **예시**: 사전수뢰죄에서의 '공무원 또는 중재인이 된 사실' (공무원이 되기 전에 청탁과 함께 뇌물을 수수/약속하면 사전수뢰죄가 성립하지만, 실제로 공무원이 되어야만 처벌 가능)\\n- **특징**: 이 객관적 조건의 발생 여부에 대해 행위자의 고의나 인식은 필요하지 않음.\\n\\n② 인적 처벌조각사유\\n- **의의**: 행위자의 특수한 신분이나 지위 때문에 범죄는 성립하더라도 처음부터 형벌권이 발생하지 않는(조각되는) 사유\\n- **예시**: 친족상도례 (가족 간의 절도, 사기 등 재산범죄는 범죄가 맞지만, '법은 가정의 문지방을 넘지 않는다'는 정책적 취지에서 형을 면제함)\\n- **특징**: 행위자 개인의 신분에만 적용되므로, 신분이 없는 공범에게는 효력이 미치지 않음 (예: 아들이 친구와 아버지 지갑을 훔친 경우 아들은 형 면제, 친구는 정상 처벌).",
    "subnoteBridge": "시험(임용) 대비 핵심 구별 포인트:\\n\\n1. **범죄성립 여부와의 관계**\\n- 위법성·책임조각사유: 범죄 성립 자체를 부정함 (무죄)\\n- 처벌조각사유: 범죄는 성립하나 형벌권만 발생하지 않음 (형 면제)\\n\\n2. **공범에 대한 효력 (친족상도례)**\\n- 인적처벌조각사유는 당해 '신분'이 있는 자에게만 개별적으로 적용됨.\\n- 따라서 친족 신분이 없는 공범에게는 처벌조각의 효력이 미치지 않고 정상 처벌됨."
  },"""

# Let's check if LAW-115 is already in there
if '"LAW-115"' in text:
    print("LAW-115 already exists in explanations-data.js")
else:
    # Insert right after `window.TOPIC_EXPLANATIONS = {`
    text = text.replace("window.TOPIC_EXPLANATIONS = {", "window.TOPIC_EXPLANATIONS = {" + insert_text, 1)
    
    with open('explanations-data.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added LAW-115 explanation")
