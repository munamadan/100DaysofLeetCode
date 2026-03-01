class Solution:
    def merge(self, nums1:list[int], nums2:list[int], m:int, n:int) -> None:
        j = 0
        for i in range(n):
            nums1[m] = nums2[j]
            j+=1
            m+=1
        nums1.sort()
        return nums1