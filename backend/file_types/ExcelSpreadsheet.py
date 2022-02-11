from openpyxl import load_workbook

from backend.file_types.File import File

class ExcelSpreadsheet(File):
    extension = 'xlsx'

    def get_text(self) -> str:
        workbook = load_workbook(filename = self.filename, data_only = True, read_only = True)
        return ' '.join(map(str, [value for worksheet in workbook.worksheets for row in worksheet.values for value in row]))