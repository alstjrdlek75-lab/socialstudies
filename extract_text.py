from pypdf import PdfReader
import sys

reader = PdfReader("/Users/mac/.gemini/antigravity/brain/4a70d882-2b4c-4198-8306-012686530f35/.user_uploaded/media_1789208325879.pdf")
text = ""
for i, page in enumerate(reader.pages):
    text += f"\n--- Page {i+1} ---\n"
    text += page.extract_text() or ""

with open("pdf_text.txt", "w") as f:
    f.write(text)
print("Text extracted to pdf_text.txt")
