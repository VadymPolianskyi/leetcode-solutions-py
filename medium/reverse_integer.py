class Solution:
    def reverse(self, x: int) -> int:

        if -10 < x < 10:
            return x

        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0

        prefix = ''
        if x < 0:
            prefix = '-'
            x = x * -1

        x_str = str(x)
        nx_str = prefix + x_str[::-1]

        nx = int(nx_str)
        if nx >= 2 ** 31 - 1 or nx <= -2 ** 31:
            return 0
        else:
            return nx
