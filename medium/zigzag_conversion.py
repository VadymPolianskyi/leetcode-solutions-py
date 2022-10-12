class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        temp_result = {}
        for n in range(numRows):
            temp_result[n] = []

        result_index = 0
        direction = True  # true (up) false (down)

        for symb in s:
            temp_result[result_index].append(symb)

            if (result_index <= 0 and not direction) or (result_index >= numRows - 1):
                direction = not direction

            if direction:
                result_index += 1
            else:
                result_index -= 1

        result = [''.join(v) for v in temp_result.values()]
        return ''.join(result)
