from resume_parser import extract_resume_data
from database import create_db, insert_candidate

pdf_file = "PRATHAM final Resume.pdf"  

create_db()
data = extract_resume_data(pdf_file)
insert_candidate(data)
print("Candidate data extracted and saved to database.")
