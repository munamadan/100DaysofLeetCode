class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_len = 0
        l = 0
        count_zero = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                count_zero += 1
            while count_zero > k:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
