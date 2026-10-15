class TAD():
    def __init__(self, name: str, definition: str):
        self.name = name
        self.definition = definition
    def __repr__(self):
        return f"{self.name} - {self.definition}"