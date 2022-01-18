from abc import ABC, abstractmethod
from typing import Optional

class File(ABC):
    def __init__(self, filename) -> None:
        self._filename: str = filename
    
    @property
    def filename(self):
        return self._filename

    @abstractmethod
    def search(text: str) -> Optional[str]:
        pass