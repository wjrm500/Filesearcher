import os

from backend.file_types.CsvFile import CsvFile
from backend.file_types.ExcelSpreadsheet import ExcelSpreadsheet
from backend.file_types.PdfFile import PdfFile
from backend.file_types.PowerPointPresentation import PowerPointPresentation
from backend.file_types.TextFile import TextFile
from backend.file_types.WordDocument import WordDocument

class FileFactory:
    @staticmethod
    def create(filename):
        extension = os.path.splitext(filename)[1][1:].lower()
        if extension == CsvFile.extension:
            return CsvFile(filename)
        elif extension == ExcelSpreadsheet.extension:
            return ExcelSpreadsheet(filename)
        elif extension == PdfFile.extension:
            return PdfFile(filename)
        elif extension == PowerPointPresentation.extension:
            return PowerPointPresentation(filename)
        elif extension == TextFile.extension:
            return TextFile(filename)
        elif extension == WordDocument.extension:
            return WordDocument(filename)
        else:
            raise Exception(f'No file class found for extension "{extension}"')