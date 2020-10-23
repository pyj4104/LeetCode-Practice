class Solution:
    def maxArea(self, height: [int]) -> int:
        #return self.maxArea_simple(height)
        return self.maxArea_complex(height)
    
    def maxArea_simple(self, height: [int]) -> int:
        retVal = 0
        maxHeight = 0
        maxIndex = 0

        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i+1:], 1):
                retVal = max(min(h1, h2)*j, retVal)
        return retVal

    def maxArea_complex(self, height: [int]) -> int:
    	left = 0
    	right = len(height) - 1
    	max_area = 0

    	while left != right:
    		max_area = max(min(height[left], height[right])*(right - left), max_area)
    		if height[left] > height[right]:
    			right -= 1
    		else:
    			left += 1

    	return max_area

cases = [[1,8,6,2,5,4,8,3,7]
		]
s = Solution()
for case in cases:
	print(s.maxArea(case))