class Solution:
    def romanToInt(self, s:str) -> int:
        romanSet = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            if i<len(s)-1 and romanSet[s[i]]<romanSet[s[i+1]]:
                res-=romanSet[i]
            else:
                res+=romanSet[i]
        return res