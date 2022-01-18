from file_types.File import File

class TextFile(File):
    extension = 'txt'

    def get_text(self) -> str:
        with open(self.filename, 'r') as file:
            file_text = file.read()
        return file_text