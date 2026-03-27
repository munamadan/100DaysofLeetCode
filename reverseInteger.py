class Solution:
    def reverseInteger(self, x: int) -> int:
        int_min, int_max = -(2**31), 2**31 - 1
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1])
        return sign * rev if int_min <= rev <= int_max else 0
