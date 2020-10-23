class Solution:
    def romanToInt(self, s: str) -> int:
        self.translation = {"I": 1,\
                            "IV": 4,\
                            "V": 5,\
                            "IX": 9,\
                            "X": 10,\
                            "XL": 40,\
                            "L": 50,\
                            "XC": 90,\
                            "C": 100,\
                            "CD": 400,\
                            "D": 500,\
                            "CM": 900,\
                            "M": 1000}
        return self.r2i(s)

    def r2i(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return self.translation[s[0]]

        retVal = 0
        moveIndexBy = 1
        char = s[len(s)-1]
        if char != "I" and len(s) > 1:
            char = s[len(s)-2:len(s)]
            if char in self.translation:
                moveIndexBy = 2
                retVal = self.translation[char]
            else:
                char = s[len(s)-1]
                retVal = self.translation[char]
        else:
            retVal = self.translation[char]

        return retVal + self.r2i(s[:len(s)-moveIndexBy])

s = Solution()
print(s.romanToInt(''))
print(s.romanToInt('I'))
print(s.romanToInt('III'))
print(s.romanToInt("IV"))
print(s.romanToInt("IX"))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))
