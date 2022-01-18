class Directory:
    def __init__(self, directory_name: str) -> None:
        self._name = directory_name
    
    @property
    def name(self):
        return self._name