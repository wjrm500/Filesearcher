import re
from typing import List, Optional

from file_types.File import File
from SearchOccurrence import SearchOccurrence

class TextFile(File):
    extension = 'txt'

    def search(self, search_string: str, chars_either_side: int = 25) -> List[SearchOccurrence]:
        search_occurrences = []
        with open(self.filename, 'r') as file:
            file_text = file.read()
            # file_text = re.sub('\s+', ' ', file_text)
            find_positions = []
            n = -1
            while (n := file_text.find(search_string, n + 1)) != -1:
                find_positions.append(n)
            for position in find_positions:
                start_index = position - chars_either_side
                while start_index > 0 and not file_text[start_index - 1].isspace():
                    start_index -= 1
                end_index = position + len(search_string) + chars_either_side
                file_text_len = len(file_text)
                while end_index < file_text_len and not file_text[end_index].isspace():
                    end_index += 1
                occurrence_text = file_text[start_index:end_index]
                search_occurrence = SearchOccurrence(self.filename, position, occurrence_text)
                search_occurrences.append(search_occurrence)
        return search_occurrences