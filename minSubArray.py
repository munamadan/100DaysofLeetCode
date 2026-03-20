class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        min_len = float("inf")
        sum = 0
        while r < n:
            sum += nums[r]
            while sum >= target:
                min_len = min(min_len, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float("inf") else 0
