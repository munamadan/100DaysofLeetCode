#solution (neetcode)
class Solution:
    def trap(self, height: list[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        trapped = 0
        for i in range(len(height)):
            if i==0:
                max_left[i] = height[i]
            max_left[i] = max(max_left[i-1], height[i])

        for i in range(len(height)-1, -1, -1):
            if i==len(height)-1:
                max_right[i] = height[i]
            max_right[i] = max(max_right[i+1], height[i])
        
        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            if water > 0:
                trapped+=water
        return trapped
    
#neetcode optimized solution
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        l,r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        trapped = 0
        while l<r:
            if maxLeft<maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                trapped+=maxLeft-height[l]
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                trapped+=maxRight - height[r]
        return trapped