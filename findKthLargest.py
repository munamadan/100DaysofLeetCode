#pythonic method
class Solution:
    def findkthlargest(self, nums:list[int], k:int)->int:
        n = len(nums)
        nums.sort()
        return nums[n-k]

#actual method
class Solution:
    def findkthlargest(self, nums:list[int], k:int) -> int:
