#sorted method

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = 0
        sort = sorted(nums)
        for i in range(1, len(sort)):
            if sort[i]==sort[i-1]:
                count = 1
        
        if count == 0:
            return False
        else:
            return True
        

#brute force method
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i==j:
                    continue
                else:
                    if nums[i]==nums[j]:
                        return True
        return False

#hashset method(neetcode)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)

#optimized set
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        else:
            return False