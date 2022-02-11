import csv

from backend.file_types.File import File

class CsvFile(File):
    extension = 'csv'

    def get_text(self) -> str:
        text_elements = []
        with open(self.filename, 'r') as file:
            data = csv.reader(file)
            for row in data:
                text_elements.append(', '.join(row))
        return '\n'.join(text_elements)