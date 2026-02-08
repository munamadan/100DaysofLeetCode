#brute force method
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] = 1 + freq_dict[num]
            else:
                freq_dict[num] = 1
        sorted_dict = sorted(freq_dict, key=freq_dict.get, reverse=True)
        return sorted_dict[:k]
    
#neetcode method
class Solution:
    def topKFrequent(self, nums: list[int], k:int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

