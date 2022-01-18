from glob import glob
import os
from Directory import Directory
from file_types.FileFactory import FileFactory

class Backend:
    def __init__(self) -> None:
        self._directory: Directory = None
        self._file_type: str = None
        self._search_string: str = None
        self._recursive: bool = False
    
    @property
    def directory(self):
        return self._directory
    
    @directory.setter
    def directory(self, directory: Directory):
        self._directory = directory
    
    @property
    def file_type(self):
        return self._file_type
    
    @file_type.setter
    def file_type(self, file_type: str):
        self._file_type = file_type
    
    @property
    def search_string(self):
        return self._search_string
    
    @search_string.setter
    def search_string(self, search_string: str):
        self._search_string = search_string
    
    @property
    def recursive(self):
        return self._recursive
    
    @recursive.setter
    def recursive(self, recursive: bool):
        self._recursive = recursive
    
    def load_file(self, filename):
        return FileFactory.create(filename)
    
    def load_files(self):
        if self.recursive:
            files = [y for x in os.walk(self.directory) for y in glob(os.path.join(x[0], f'*.{self.file_type}'))]
        else:
            files = [
                file for f in os.listdir(self.directory)
                if os.path.isfile((file := os.path.join(self.directory, f)))
                and os.path.splitext(f)[1][1:] == self.file_type
                ]
        return map(self.load_file, files)
    
    def search_files(self):
        # missing_attrs = [attr for attr in [self.directory, self.file_type, self.search_string] if attr is None]
        if self.directory is None:
            raise Exception('Missing directory attribute on Backend object')
        if self.file_type is None:
            raise Exception('Missing file_type attribute on Backend object')
        if self.search_string is None:
            raise Exception('Missing search_string attribute on Backend object')
        file_objects = self.load_files()
        total_occurrences = []
        for file_object in file_objects:
            occurrences = file_object.search(self.search_string)
            total_occurrences.extend(occurrences)
        return total_occurrences
