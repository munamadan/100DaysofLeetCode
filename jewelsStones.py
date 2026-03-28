#my solution
class Solution:
    def jewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = {}
        count = 0
        for jewel in jewels:
            jewelSet[jewel] = 1 + jewelSet.get(jewel, 0)
        for i in range(len(stones)):
            if stones[i] in jewelSet: count += 1
        return count
#optimized method
class Solution:
    def jewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewelSet = set(jewels)
        for stone in stones:
            if stone in jewelSet: count += 1
        return count
