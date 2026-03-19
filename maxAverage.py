class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]

        avg_sum = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]

            avg_sum = max(avg_sum, cur_sum / k)

        return avg_sum
