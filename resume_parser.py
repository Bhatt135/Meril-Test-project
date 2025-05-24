import fitz  # PyMuPDF
import re

def extract_resume_data(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Simple extractions (can be improved with NLP)
    name = text.split('\n')[0].strip()  # Assuming name is first line
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    phone = re.search(r'\b\d{10}\b', text)

    return {
        "name": name,
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "raw_text": text
    }
