class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i=0
        while i < len(s):
            if s[i]==' ':
                i+=1
                continue
            start = i
            while i<len(s) and s[i]!=' ':
                i+=1
            words.append(s[start:i])
        words.reverse()
        return " ".joins(words)