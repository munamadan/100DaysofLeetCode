#brute force method
class Solution:
    def majorityElement(self, nums:list[int]) -> int:
        numSet = {}
        for i in range(len(nums)):
            if nums[i] in numSet:
                numSet[nums[i]] = 1 + numSet.get(nums[i], 0)
            else:
                numSet[nums[i]] = 1
        return max(numSet, key=numSet.get)
    
#optimized solution
class Solution:
    def majorityElement(self, nums:list[int]) -> int:
        numSet = {}
        for num in nums:
            numSet[num] = 1 + numSet.get(num, 0)
        return max(numSet, key=numSet.get)