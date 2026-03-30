class Solution:
    def maxNumberOfBalloons(self, text:str) -> int:
        charSet = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for i in range(len(text)):
            if text[i] in charSet:
                charSet[text[i]] += 1
        return min(charSet['b'], charSet['a'], charSet['l']//2, charSet['o']//2, charSet['n'])
