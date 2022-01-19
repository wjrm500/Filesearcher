# from tika import parser
from pdf2image import convert_from_path
import pytesseract

from file_types.File import File

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class PdfFile(File):
    extension = 'pdf'

    def get_text(self) -> str:
        pages = convert_from_path(self.filename, 300, poppler_path = 'C:\\Program Files\\poppler-22.01.0\\Library\\bin')
        return '\n'.join([pytesseract.image_to_string(page) for page in pages])

        # raw = parser.from_file(self.filename)
        # return raw['content']