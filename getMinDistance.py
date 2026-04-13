class Solution:
    def getMinDistance(self, nums:list[int], start:int, target:int) -> int:
        min_len = float('inf')
        for i in range(len(nums)):
            if nums[i]==target: min_len = min(min_len, abs(i-start))
        return min_len
