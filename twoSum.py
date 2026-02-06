#brute force method
class Solution:
    def twoSum(self, nums: list[int], target:int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return i,j
                    
#hashmap method(neetcode)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashmap:
                return i, hashmap[needed]
            else:
                hashmap[nums[i]] = i