class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        # Overload += operator
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        return self

    def toLower(self):
        result = ""
        for ch in self.value:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result

    def toUpper(self):
        result = ""
        for ch in self.value:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            else:
                result += ch
        return result

    def __str__(self):
        return self.value

s1 = String("Hello")
s2 = String(" World!")

print(f"Original s1: {s1}")
s1 += s2
print(f"After s1 += s2: {s1}")

print(f"Lowercase: {s1.toLower()}")
print(f"Uppercase: {s1.toUpper()}")