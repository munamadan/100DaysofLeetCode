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


# optimized solution
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, cur_sum)
        return max_sum / k
