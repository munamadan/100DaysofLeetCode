class Solution:
    def missingNumber(self, nums:list[int]) -> int:
        num.sort()
        for i in range(len(nums)):
            if i!=nums[i]: return i
        return i+1
