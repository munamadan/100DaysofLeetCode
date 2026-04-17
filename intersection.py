#hash map approach
class Solution:
    def intersection(self, num1:list[int], nums2:list[int]) -> list[int]:
        res = []
        count = {}
        for num in nums1:
            count[num] = 1 + count.get(num, 0)
        for num in nums2:
            if num in count:
                res.append[num]
                del count[num]
        return res

#set method approach
class Solution:
    def intersection(self, nums1:list[int], nums2:list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
