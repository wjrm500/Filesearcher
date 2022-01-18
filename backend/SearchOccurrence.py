class SearchOccurrence:
    def __init__(self, filename: str, position: int, text: str) -> None:
        self._filename = filename
        self._position = position
        self._text = text
    
    @property
    def text(self):
        return f'...{self._text}...'