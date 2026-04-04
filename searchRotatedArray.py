class Solution:
    def search(self, nums:list[int], target:int) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]: r = mid
            elif nums[mid]>nums[r]: l = mid+1
        min_index = l
        if min_index==0: l,r = 0, len(nums)-1
        elif target>=nums[0] and target<=nums[min_index-1]: l,r = 0, min_index-1
        else: l,r = min_index, len(nums)-1
        while l<=r:
            midd = (l+r)//2
            if nums[midd]<target: l=midd+1
            elif nums[midd]>target: r = midd-1
            elif nums[midd]==target: return midd
        return -1
