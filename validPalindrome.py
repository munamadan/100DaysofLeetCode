import re

#brute force method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[^a-z0-9]", "", s.lower)
        for i in range(len(cleaned)):
            if cleaned[i]!=cleaned[len(cleaned)-1-i]:
                return False
        return True
    
#brutally optimized
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
        return cleaned == cleaned[::-1]
    
#two pointer (neetcode method)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left<right:
            while left<right and not self.alphanum(s[left]):
                left+=1
            while right>left and not self.alphanum(s[right]):
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
                
    def alphanum(self, c) -> bool:
        return ((ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')))