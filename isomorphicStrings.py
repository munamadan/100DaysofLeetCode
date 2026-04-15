class Solution:
    def isomorphicStrings(self, s:str, t:str) -> bool:
        char_s = {}
        char_t = {}
        for cs, ct in zip(s, t):
            if cs in char_s:
                if char_s[cs]!=ct: return False
            else: char_s[cs] = ct

            if ct in char_t:
                if char_t[ct]!=cs: return False
            else: char_t[ct]=cs
        return True
