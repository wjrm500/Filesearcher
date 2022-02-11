from glob import glob
import os
from typing import List

from backend.Directory import Directory
from backend.file_types.FileFactory import FileFactory
from backend.SearchOccurrence import SearchOccurrence

class Backend:
    def __init__(self) -> None:
        self._directory: Directory = None
        self._file_types: List[str] = []
        self._search_string: str = None
    
    @property
    def directory(self):
        return self._directory
    
    @directory.setter
    def directory(self, directory: Directory):
        self._directory = directory
    
    @property
    def file_types(self):
        return self._file_types
    
    @file_types.setter
    def file_types(self, file_types: List[str]):
        self._file_types = file_types
    
    @property
    def search_string(self):
        return self._search_string
    
    @search_string.setter
    def search_string(self, search_string: str):
        self._search_string = search_string
    
    def load_file(self, filename):
        return FileFactory.create(filename)
    
    def load_files(self, recursive: bool = False):
        if recursive:
            files = []
            for x in os.walk(self.directory):
                for file_type in self.file_types:
                    new_files = glob(os.path.join(x[0], f'*.{file_type}'))
                    new_files = [file for file in new_files if not '\\~$' in file]
                    files.extend(new_files)
        else:
            files = [
                file for f in os.listdir(self.directory)
                if not f.startswith('~$')
                and os.path.isfile((file := os.path.join(self.directory, f)))
                and os.path.splitext(f)[1][1:] in self.file_types
                ]
        return map(self.load_file, files)
    
    def search_files(self, recursive: bool = False, chars_either_side: int = 25, ignore_case: bool = False) -> List[SearchOccurrence]:
        if self.directory is None:
            raise Exception('Missing directory attribute on Backend object')
        if self.file_types is None:
            raise Exception('Missing file_type attribute on Backend object')
        if self.search_string is None:
            raise Exception('Missing search_string attribute on Backend object')
        file_objects = self.load_files(recursive)
        all_occurrences = []
        for file_object in file_objects:
            occurrences = file_object.search(self.search_string, chars_either_side, ignore_case)
            all_occurrences.extend(occurrences)
        return all_occurrences