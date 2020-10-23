class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
        	return "1"
        else:
        	prevAns = self.countAndSay(n-1)

        index = -1
        ans = ''
        curLet = prevAns[0]
        curCounter = 0

        for i, letter in enumerate(prevAns):
        	if letter == curLet:
        		curCounter += 1
        	else:
        		ans += str(curCounter) + str(curLet)
        		curLet = letter
        		curCounter = 1
        ans += str(curCounter) + str(curLet)

        return ans
