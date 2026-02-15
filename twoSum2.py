#brute force method
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        num_set = {}
        for i in range(len(numbers)):
            needed = target - numbers[i]
            if needed in num_set:
                return [i+1, num_set[needed]+1]
            num_set[numbers[i]] = i
#neetcode
class Solution:
    def twoSum(self, numbers: list[int], target: list[int]) -> list[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum>target:
                r-=1
            elif curSum<target:
                l+=1
            else:
                return [l+1, r+1]