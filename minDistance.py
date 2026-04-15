class Solution:
    def closestTarget(self, words:list[str], target:str, startIndex:int) -> int:
        min_distance = float('inf')
        n = len(words)
        for i in range(len(words)):
            if words[i]==target:
                dist = min(abs(i-startIndex), n-abs(i-startIndex))
                min_distance = min(min_distance, dist)
        return min_distance if min_distance!=float('inf') else -1
