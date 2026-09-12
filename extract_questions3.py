import re

with open("pdf_text.txt", "r") as f:
    lines = f.readlines()

output = []
state = 'OUT'
current_block = []

past_q_pattern = re.compile(r'^\s*\d+\s*•\s*\d{4}년')
test_pattern = re.compile(r'^\s*[【\[〔\(]?\s*응용\s*TEST\s*\d+\s*[】\]〕\)]?')

def save_block():
    if current_block:
        clean_block = []
        for line in current_block:
            line_str = line.strip()
            if line_str.startswith('ZMEMO') or line_str.startswith('MEMO') or line_str.startswith('/MEMO') or line_str.startswith("' MEMO") or line_str.startswith("『MEMO"): continue
            if re.match(r'^Chapter \d+\.', line_str): continue
            if re.match(r'^\d+\s+Part \d+\.', line_str): continue
            if re.match(r'^아lapter \d+\.', line_str): continue
            if re.match(r'^--- Page \d+ ---$', line_str): continue
            if "미시경제학" in line_str and len(line_str) < 20: continue
            if "거시경제학" in line_str and len(line_str) < 20: continue
            if "임용 경제학" in line_str and len(line_str) < 20: continue
            if line_str == "02": continue
            if line_str == "CHAPTER": continue
            if re.match(r'^\d+\s*국민소득', line_str): continue
            clean_block.append(line)
        if clean_block:
            output.append("".join(clean_block).strip())
        current_block.clear()

for line in lines:
    clean = line.strip()
    
    # fix OCR typos
    clean = clean.replace("g •", "9 •").replace('"J •', "1 •").replace('y •', "7 •")
    
    if past_q_pattern.match(clean) or test_pattern.match(clean):
        save_block()
        if past_q_pattern.match(clean):
            state = 'Q'
        else:
            state = 'TEST'
        current_block.append(line)
    elif "개념-이론" in clean or "기출분석" in clean or "정답 및 해설" in clean or "개념 - 이론" in clean or "기출 분석" in clean or "개념—이론" in clean or "개념ᅳ이론" in clean:
        if state in ('Q', 'TEST'):
            save_block()
            state = 'OUT'
    else:
        if state in ('Q', 'TEST'):
            current_block.append(line)

save_block()

with open("/Users/mac/.gemini/antigravity/brain/4a70d882-2b4c-4198-8306-012686530f35/extracted_economics_questions.md", "w") as f:
    f.write("# 추출된 기출문제 및 응용 TEST\n\n")
    for block in output:
        if block:
            # Fix OCR for the first line of block if needed
            block_lines = block.split('\n')
            block_lines[0] = block_lines[0].replace("g •", "9 •").replace('"J •', "1 •").replace('y •', "7 •")
            f.write('\n'.join(block_lines))
            f.write("\n\n---\n\n")

print(f"Extracted {len(output)} items.")
