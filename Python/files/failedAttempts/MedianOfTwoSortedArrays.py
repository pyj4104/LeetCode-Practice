class Solution:
    def findMedianSortedArrays_no(self, nums1: [int], nums2: [int]) -> float:
        arr = self.__merge__(nums1, nums2)
        
        if (len(arr) % 2) == 1:
            middle = int(len(arr)/2)
            return arr[middle]
        else:
            middleU = int(len(arr)/2)
            middleL = middleU-1
            return (arr[middleU] + arr[middleL]) / 2

    def __merge__(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.append(None)
        nums2.append(None)

        nums1Index = 0
        nums2Index = 0

        retVal = []

        while nums1[nums1Index] is not None or nums2[nums2Index] is not None:
            num1 = nums1[nums1Index]
            num2 = nums2[nums2Index]

            if num1 is None:
                while nums2[nums2Index] is not None:
                    retVal.append(nums2[nums2Index])
                    nums2Index += 1

            if num2 is None:
                while nums1[nums1Index] is not None:
                    retVal.append(nums1[nums1Index])
                    nums1Index += 1

            if num1 is not None and num2 is not None:
                if num1 <= num2:
                    retVal.append(num1)
                    nums1Index += 1
                elif num2 < num1:
                    retVal.append(num2)
                    nums2Index += 1

        return retVal

    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        lower, higher, lowerMid, higherMid = self.__findMid__(nums1, nums2)
        print(lower, higher, lowerMid, higherMid)

        return __findMedianSortedArrays__(lower, higher, lowerMid, higherMid)

    def __findMid__(self, nums1: [int], nums2: [int]):
        totLen = len(nums1) + len(nums2)
        nums1Len = len(nums1)
        nums2Len = len(nums2)

        if nums1Len < nums2Len:
        	lower = nums1
        	higher = nums2
        	lowerLen = len(nums1)
        	higherLen = len(nums2)
        else:
        	lower = nums2
        	higher = nums1
        	lowerLen = len(nums2)
        	higherLen = len(nums1)

        lowerMid = int(lowerLen/2)
        higherMid = int((higherLen/2))

        return lower, higher, lowerMid, higherMid

    def __findMedianSortedArrays__(self, lower: [int], higher: [int], lowerMid: int, higherMid: int) -> float:
    	# In case it's not possible - lowerMid is pushed to the end.
    	if lowerMid + 1 == len(lower):
    		tot = lower + higher
    		return tot[int(tot/2)] if (len(tot)%2) else (tot[int(tot/2)]+tot[int(tot/2)+1])/2
    	# In case it's not possible - higherMid is pushed to the end.
    	if higherMid + 1 == len(lower):
    		tot = higher + lower
    		return tot[int(tot/2)] if (len(tot)%2) else (tot[int(tot/2)]+tot[int(tot/2)+1])/2

    	if lower[lowerMid] <= higher[higherMid+1] and higher[higherMid] <= lower[lowerMid+1]:
    		tot = len(lower) + len(higher)
    		if (len(tot)%2):
    			return (max(lower[lowerMid], higher[higherMid]))
    		else
    			return (max(lower[lowerMid], higher[higherMid]) + min(lower[lowerMid+1], higher[higherMid+1]))/2
    	else:
    		if lower[lowerMid] >= higher[higherMid+1]

sol = Solution()

print(sol.findMedianSortedArrays([1,2,3],[3, 4, 5, 6, 7]))
