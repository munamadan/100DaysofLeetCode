class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        l = 0
        for ch in t:
            if l < len(s) and s[l] == ch:
                l += 1
            if l == len(s):
                return True

        return False
