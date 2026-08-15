class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        rows = [""] * numRows
        row = 0
        direction = 1

        for letter in s:
            rows[row] = rows[row] + letter

            if row == 0:
                direction = 1

            if row == numRows - 1:
                direction = -1

            row = row + direction

        return "".join(rows)
