from msilib import make_id


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
class Solution:
    def searchInsert(self, nums:list[int], target:int) -> int:
        l,r = 0, len(nums)-1
        while l<=right:
            m = (l+r)//2
            if nums[m]<target: l=mid+1
            elif nums[m]>target: r=mid-1
            else: return m

        return l
