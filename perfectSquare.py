class Solution:
    def perfectSquare(self, num:int) -> bool:
        if num==0 or num==1: return True
        l,r = 0, num-1
        while l<=r:
            mid = (l+r)//2
            if mid**2>num: r = mid-1
            elif mid**2<num: l = mid+1
            else: return True
        return False
