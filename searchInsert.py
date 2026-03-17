class Solution:
    def searchInsert(self, nums:list[int], target:int) -> int:
        n = len(nums)
        if target>nums[-1]: return n
        for i in range(n):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i

#ez af