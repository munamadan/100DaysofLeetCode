#brute force
class Solution:
    def longestConsecutive(self, nums : list[int]) -> int:
        if len(nums) == 0:
            return 0
        res = sorted(set(nums))
        current_length, maximum_length = 1, 1
        for i in range(1, len(res)):
            if (res[i] - res[i-1])==1:
                current_length += 1
                maximum_length = max(current_length, maximum_length)
            else:
                current_length = 1
        return maximum_length


#neetcode method in O(n) time
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n-1) not in numSet:
                length = 0 
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

