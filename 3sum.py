class Solution: 
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-1):
            seen = set()
            for j in range(i+1, range(len(nums))):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.add((nums[i], nums[j], complement))
                else:
                    seen.add(nums[j])
        return list(res)
    
#neetcode method
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, a in nums:
            if i>0 and a==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                threeSum = a+nums[l]+nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
    
#short note: this question is way harder than it looks, do twosum2 before this 
#to understan the two pointer technique, even though I did that I still couldn't do it lmao
#fuck this question