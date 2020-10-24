class Solution:
    def rob2(self, nums: [int]) -> int:
        return max(self.rob([:len(nums)-1]), self.rob([1:len(nums)]))

    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i]+nums[i-2], nums[i-1])

        return nums[-1]