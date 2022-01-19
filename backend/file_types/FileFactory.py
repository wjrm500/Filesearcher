import os

from file_types.CsvFile import CsvFile
from file_types.ExcelSpreadsheet import ExcelSpreadsheet
from file_types.PdfFile import PdfFile
from file_types.PowerPointPresentation import PowerPointPresentation
from file_types.TextFile import TextFile
from file_types.WordDocument import WordDocument

class FileFactory:
    @staticmethod
    def create(filename):
        extension = os.path.splitext(filename)[1][1:]
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