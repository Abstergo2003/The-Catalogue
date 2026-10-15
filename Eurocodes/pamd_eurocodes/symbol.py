class Symbol():
    def __init__(self, latex: str, description: str):
        self.latex = latex
        self.description = description
    def __repr__(self):
        return f"$ {self.latex} $ - {self.description}"