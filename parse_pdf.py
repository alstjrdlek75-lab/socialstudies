import re

with open("pdf_text.txt", "r") as f:
    text = f.read()

# Let's find all past questions and application tests
# A past question starts with "XX • YYYY년" or similar. Let's find all occurrences of "•" or "년" in a short line.
# Also "【응용 TEST"
past_q_pattern = re.compile(r'^(\d+\s*•\s*\d{4}년.*)$', re.MULTILINE)
apply_test_pattern = re.compile(r'^(【응용 TEST.*)$', re.MULTILINE)

past_qs = past_q_pattern.findall(text)
apply_tests = apply_test_pattern.findall(text)

print(f"Found {len(past_qs)} past questions.")
for q in past_qs[:5]:
    print(q)

print(f"\nFound {len(apply_tests)} application tests.")
for t in apply_tests[:5]:
    print(t)
