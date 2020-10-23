class Solution:
    ROSSETTA_STONE = {\
                      1: ["I", "X", "C", "M"],\
                      2: ["II", "XX", "CC", "MM"],\
                      3: ["III", "XXX", "CCC", "MMM"],\
                      4: ["IV", "XL", "CD"],\
                      5: ["V", "L", "D"],\
                      6: ["VI", "LX", "DC"],\
                      7: ["VII", "LXX", "DCC"],\
                      8: ["VIII", "LXXX", "DCCC"],\
                      9: ["IX", "XC", "CM"]\
                     }
    
    def intToRoman(self, num: int) -> str:
        digit = 0
        retVal = ""
        while num != 0:
            numAtDigit = num%10
            if not numAtDigit == 0:
                retVal = self.ROSSETTA_STONE[numAtDigit][digit] + retVal
            num = int(num/10)
            digit += 1
        return retVal
s = Solution()
for i in range(1, 4000):
  print(s.intToRoman(i))