import PyPDF2
import re

# Replace 'example.pdf' with the path to your PDF file
pdf_path = 'example.pdf'

# Regular expression to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def extract_emails_from_pdf(pdf_path):
    emails = set()
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            emails.update(re.findall(email_pattern, text))

    return emails

found_emails = extract_emails_from_pdf(pdf_path)
print(f"<===|Number of email addresses found in the PDF:{len(found_emails)}|===>")
if found_emails:
    print("Email addresses found in the PDF:")
    for email in found_emails:
        print(email)
else:
    print("No email addresses found in the PDF.")
