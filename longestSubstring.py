# brute force method
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        chars = set()
        maxLen = 0
        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            maxLen = max(r - l + 1, maxLen)
            chars.add(s[r])
            r += 1
        return maxLen


# neetcode method(not much difference, he just didn't have the checker for 0 length and maxLen is set at 0)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res
