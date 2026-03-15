#brute force method (timeout hunchha)
class Solution:
    def rotate(self, nums:list[int], k:int) -> None:
        while k!=0:
            last = nums[-1]
            for i in range(len(nums)-1, -1, -1):
                if k==0: return nums
                nums[i] = nums[i-1]
            nums[0] = last
            k-=1

class Solution:
    def rotate(self, nums:list[int], k:int) -> None:
        k = k%n
        n = len(nums)
        temp = [0]*n
        for i in range(len(nums)):
            temp[(i+k)%n] = nums[i]
        for i in range(n):
            nums[i] = temp[i]
        