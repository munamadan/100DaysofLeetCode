#brute force
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
    
#neetcode(idk what the hell he is doing here, my brute force method is much simpler and easier to understand)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(s)
        return list(res.values())