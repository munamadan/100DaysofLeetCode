#counter method (don't use  this in interviews)
import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))

#hashmpa method
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charSet = {}
        for i in range(len(magazine)):
            charSet[magazine[i]] = 1 + charSet.get(magazine[i], 0)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in charSet: return False
            elif ransomNote[i] in charSet:
                charSet[ransomNote[i]] -= 1
                if charSet[ransomNote[i]] == 0: del charSet[ransomNote[i]]
        return True
