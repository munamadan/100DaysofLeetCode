#neetcode/brute foce, be careful with the edge cases it is very deceiving
class Solution:
    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    def decode(self, s:str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = s[i:j]
            result.append(str[j+1: j+1+length])
            i = j+1+length
        return result
