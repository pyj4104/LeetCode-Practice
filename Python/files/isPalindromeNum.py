class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x < 10:
            return True

        numList = []
        g = x
        while g != 0:
            numList.append(g%10)
            g = int(g/10)
        
        left = 0
        right = len(numList) - 1

        while not(left == right or left+1 == right):
            if numList[left] != numList[right]:
                return False
            left += 1
            right -= 1
        
        return True

s = Solution()
print(s.isPalindrome(10))