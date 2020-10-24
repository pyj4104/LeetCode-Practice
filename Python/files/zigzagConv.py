class Solution:
    def convert_f(self, s: str, numRows: int) -> str:
        if s == '':
            return ''

        if numRows <= 0:
            raise AssertionError

        if numRows == 1:
            return s

        retVal = [''] * numRows
        lenSegment = (2 * numRows) - 2
        j = 0
        while j < len(s):
            segment = s[j:min(j+lenSegment, len(s))]
            j += lenSegment

            rowIndex = 0
            left = 0
            right = lenSegment - 1
            while rowIndex < numRows:
                if rowIndex == 0:
                    retVal[rowIndex] += segment[left]
                    left += 1
                elif rowIndex+1 == numRows:
                    if rowIndex < len(segment):
                        retVal[rowIndex] += segment[rowIndex]
                else:
                    if left < len(segment):
                        retVal[rowIndex] += segment[left]
                    left += 1
                    if right < len(segment):
                        retVal[rowIndex] += segment[right]
                    right -= 1
                rowIndex += 1

        retVal_org = ''
        for val in retVal:
            retVal_org += val

        return retVal_org

    def convert(self, s: str, numRows: int) -> str:
        if s == '':
            return ''

        if numRows <= 0:
            raise AssertionError

        if numRows == 1:
            return s

        retVal = ''
        lenSegment = (2 * numRows) - 2
        j = 0
        '''while j < len(s):
            segment = s[j:min(j+lenSegment, len(s))]
            j += lenSegment'''

        rowIndex = 0
        left = 0
        right = lenSegment - 1

        while rowIndex < numRows:
            j = 0
            segIndex = 0
            while j < len(s):
                segment = s[j:min(j+lenSegment, len(s))]
                if rowIndex == 0:
                    retVal += segment[left]
                elif rowIndex+1 == numRows:
                    if rowIndex < len(segment):
                        retVal += segment[rowIndex]
                else:
                    if left < len(segment):
                        retVal += segment[left]
                    if right < len(segment):
                        retVal += segment[right]
                j += lenSegment
                segIndex += 1
            if rowIndex == 0:
                left += 1
            else:
                left += 1
                right -= 1
            rowIndex += 1

        return retVal

s = Solution()
assert(s.convert_f('PAYPALISHIRING', 3) == s.convert('PAYPALISHIRING', 3))
assert(s.convert_f('PAYPALISHIRING', 4) == s.convert('PAYPALISHIRING', 4))
assert(s.convert_f('RACINGTOCOMBATCOVID19', 5) == s.convert('RACINGTOCOMBATCOVID19', 5))
