import re

with open("pdf_text.txt", "r") as f:
    lines = f.readlines()

output = []
state = 'OUT' # 'OUT', 'Q', 'TEST'
current_block = []

def save_block():
    if current_block:
        # clean up footers from current_block
        clean_block = []
        for line in current_block:
            line_str = line.strip()
            if line_str.startswith('ZMEMO'): continue
            if re.match(r'^Chapter \d+\.', line_str): continue
            if re.match(r'^\d+\s+Part \d+\.', line_str): continue
            if re.match(r'^--- Page \d+ ---$', line_str): continue
            clean_block.append(line)
        output.append("".join(clean_block))
        current_block.clear()

past_q_pattern = re.compile(r'^\d+\s*•\s*\d{4}년')
test_pattern = re.compile(r'^[【\[〔\(]?\s*응용\s*TEST\s*\d+\s*[】\]〕\)]?')
stop_pattern = re.compile(r'^(\d*\s*개념-?이론\s*정리|기출분석|정답 및 해설)')

for line in lines:
    clean = line.strip()
    if past_q_pattern.match(clean) or test_pattern.match(clean):
        save_block()
        if past_q_pattern.match(clean):
            state = 'Q'
        else:
            state = 'TEST'
        current_block.append(line)
    elif stop_pattern.search(clean) or "기출분석" in clean and len(clean) < 15:
        if state in ('Q', 'TEST'):
            save_block()
            state = 'OUT'
    else:
        if state in ('Q', 'TEST'):
            current_block.append(line)

save_block()

with open("extracted_questions.md", "w") as f:
    f.write("# 추출된 기출문제 및 응용 TEST\n\n")
    for block in output:
        f.write(block)
        f.write("\n---\n\n")

print(f"Extracted {len(output)} items.")
