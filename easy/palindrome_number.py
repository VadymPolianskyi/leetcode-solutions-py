class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        s_i = 0
        e_i = len(x_str) - 1
        while s_i < e_i:
            if x_str[s_i] != x_str[e_i]:
                return False
            s_i += 1
            e_i -= 1
        return True
