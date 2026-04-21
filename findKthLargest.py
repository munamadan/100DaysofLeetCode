#pythonic method
class Solution:
    def findkthlargest(self, nums:list[int], k:int)->str:
        n = len(nums)
        nums.sort()
        return nums[n-k]
