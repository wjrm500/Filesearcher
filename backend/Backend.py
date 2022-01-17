from backend.Directory import Directory
from backend.FileExtension import FileExtension

class Backend:
    def __init__(self) -> None:
        Directory: self._directory = None
        FileExtension: self._file_extension = None
        str: self._search_string = None
    
    @property
    def directory(self):
        return self._directory
    
    @directory.setter
    def directory(self, directory: Directory):
        self._directory = directory
    
    @property
    def file_extension(self):
        return self._file_extension
    
    @file_extension.setter
    def file_extension(self, file_extension: FileExtension):
        self._file_extension = file_extension
    
    @property
    def search_string(self):
        return self._search_string
    
    @search_string.setter
    def search_string(self, search_string: str):
        self._search_string = search_string