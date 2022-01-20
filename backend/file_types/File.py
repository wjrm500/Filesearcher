from abc import ABC, abstractmethod
import re
from typing import List

from SearchOccurrence import SearchOccurrence

class File(ABC):
    def __init__(self, filename) -> None:
        self._filename: str = filename
    
    @property
    def filename(self) -> str:
        return self._filename
    
    @abstractmethod
    def get_text(self) -> str:
        pass

    def search(self, search_string: str, chars_either_side: int = 25, ignore_case: bool = False) -> List[SearchOccurrence]:
        search_occurrences = []
        try:
            file_text = re.sub('\s+', ' ', self.get_text())
            find_positions = []
            n = -1
            if ignore_case:
                lowercase_file_text = file_text.lower()
                lowercase_search_string = search_string.lower()
                while (n := lowercase_file_text.find(lowercase_search_string, n + 1)) != -1:
                    find_positions.append(n)
            else:
                while (n := file_text.find(search_string, n + 1)) != -1:
                    find_positions.append(n)
            for position in find_positions:
                start_index = position - chars_either_side
                while start_index > 0 and not file_text[start_index - 1].isspace():
                    start_index -= 1
                start_index = max(0, start_index)
                end_index = position + len(search_string) + chars_either_side
                file_text_len = len(file_text)
                end_index = min(file_text_len, end_index)
                while end_index < file_text_len and not file_text[end_index].isspace():
                    end_index += 1
                occurrence_text = file_text[start_index:end_index]
                search_occurrence = SearchOccurrence(self.filename, position, occurrence_text)
                search_occurrences.append(search_occurrence)
        except:
            pass
        return search_occurrences