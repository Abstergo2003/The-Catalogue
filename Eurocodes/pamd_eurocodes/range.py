def underline(text):
    # \033[4m turns on underline, \033[0m resets formatting
    return f"\033[4m{text}\033[0m"



class BRange():
    def __init__(self, min: float, max: float, default: float):
        self.min = min
        self.max = max
        self.default = default

    def __repr__(self):
        if self.default == self.max:
            return f"<{self.min}, {underline(self.max)}>"
        elif self.default == self.min:
            return f"<{underline(self.min)}, {self.max}>"
        else:
            return f"<{self.min}, {self.max}>({underline(self.default)})"

    def _extract(self, other) -> float:
        return float(other.default) if isinstance(other, BRange) else float(other)

    def __add__(self, other):
        return float(self.default) + self._extract(other)

    def __radd__(self, other):
        return self._extract(other) + float(self.default)

    def __sub__(self, other):
        return float(self.default) - self._extract(other)

    def __rsub__(self, other):
        return self._extract(other) - float(self.default)

    def __mul__(self, other):
        return float(self.default) * self._extract(other)

    def __rmul__(self, other):
        return self._extract(other) * float(self.default)

    def __truediv__(self, other):
        return float(self.default) / self._extract(other)

    def __rtruediv__(self, other):
        return self._extract(other) / float(self.default)

    def __pow__(self, power):
        return float(self.default) ** self._extract(power)

    def __neg__(self):
        return -float(self.default)
        
    def __abs__(self):
        return abs(float(self.default))

if __name__ == "__main__":
    r = BRange(2, 5, 3)
    print(r)