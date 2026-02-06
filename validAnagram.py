#sorted method
class Solution:
    def validAnagram(self, s:str, t:str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False
        
#brute force method
class Solution:
    def validAnagaram(self, s:str, t:str) -> bool:
        if len(s)!=len(t):
            return False
        
        t_list = list(t)

        for char in s:
            found=False
            for j in range(len(t_list)):
                if char==t_list[j]:
                    t_list[j]=None
                    found=True
                    break
            if not found:
                return False
            
        return True

#neetcode hashmap
class Solution:
    def validAnagram(self, s:str, t:str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            countT, countS = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c]!=countT.get(c, 0):
                return False
            
        return True