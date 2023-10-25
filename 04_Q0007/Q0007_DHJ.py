class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        minus = 0
        if x < 0:
            x = abs(x)
            minus = 1
        x_str = str(x)
        x_str = int(x_str[::-1])
        if x_str > INT_MAX:
            return 0
        if minus == 1:
            return x_str * -1
        return x_str