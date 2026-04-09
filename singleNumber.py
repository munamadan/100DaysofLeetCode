class Solution:
    def singleNumber(self, nums:list[int]) -> int:
        numSet = {}
        for num in nums:
            numSet[num] = 1 + numSet.get(num, 0)
        return min(numSet, key=numSet.get)
