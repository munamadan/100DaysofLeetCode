#brute force method
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        l,r = 0, len(height)-1
        while l<r:
            if height[l]<height[r]:
                maximum = max(height[l]*(r-l), maximum)
                l+=1
            elif height[r]<=height[l]:
                maximum = max(height[r]*(r-l), maximum)
                r-=1
        return maximum

#neetcode method
class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        while l<r:
            current = (r-l)*min(height[l], height[r])
            res = max(res, current)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res


#honestly both are almost same for runtime and space
#first leetcode medium i did on first try without any kind of help