#brute force
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        postfix = [1]
        res = []
        for i in range(len(nums)):
            prefix.append(prefix[-1]*nums[i])
        for j in reversed(range(len(nums))):
            postfix.append(postfix[-1]*nums[j])
        postfix.reverse()
        for i in range(len(nums)):
            res.append(prefix[i]* postfix[i+1])
        return res
    
#neetcode method
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
