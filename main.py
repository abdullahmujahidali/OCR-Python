import PyPDF2
from pdf2image import convert_from_path
import pytesseract

pdf_path = 'cv.pdf'
pdf_file = open(pdf_path, 'rb')

# PyPDF2 for text extraction
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()


pdf_file.close()

images = convert_from_path(pdf_path)
for img in images:
    img_text = pytesseract.image_to_string(img)
    text += img_text

print(text)
