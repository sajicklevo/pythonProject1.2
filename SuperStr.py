class SuperStr(str):
    def is_repeatance(self, s):
        if len(self) % len(s) == 0:
            return s * (len(self) // len(s)) == self
        else:
            return False

    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]

s = SuperStr("ababab")
s2 = SuperStr("aba")
print(s.is_repeatance("ab"))
print(s.is_repeatance("ba"))
print(s2.is_palindrom())
print(s.is_palindrom())