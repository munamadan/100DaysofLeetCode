#pythonic method
class Solution:
    def findkthlargest(self, nums:list[int], k:int)->int:
        n = len(nums)
        nums.sort()
        return nums[n-k]

#actual method(heap method)
class Solution:
    def findkthlargest(self, nums:list[int], k:int) -> int:
        heap = []
        for num in nums:
            heapq.push(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
