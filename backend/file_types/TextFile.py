from typing import Optional
from file_types.File import File

class TextFile(File):
    extension = 'txt'

    def search(self, text: str) -> Optional[str]:
        with open(self.filename, 'r') as f:
            a = 1