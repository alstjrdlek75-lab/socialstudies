import os
import glob
from pypdf import PdfReader

pdf_files = glob.glob("/Users/mac/.gemini/antigravity/brain/4a70d882-2b4c-4198-8306-012686530f35/.user_uploaded/*.pdf")
pdf_files.sort(key=os.path.getmtime, reverse=True)

for pdf in pdf_files[:10]:
    try:
        reader = PdfReader(pdf)
        print(f"{os.path.basename(pdf)}: {len(reader.pages)} pages")
    except Exception as e:
        print(f"{os.path.basename(pdf)}: Error {e}")
