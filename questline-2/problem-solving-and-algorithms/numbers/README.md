# Number Algorithms

This folder contains my solutions for the Number Algorithms challenge.

## Problems Solved

### 1. Palindrome Number

The goal of this problem is to check whether a given integer is a palindrome.

A palindrome reads the same from left to right and right to left.

Example:

121 -> Palindrome  
123 -> Not Palindrome

### Approach

1. Convert the integer into a string.
2. Reverse the string using Python slicing.
3. Compare the original string with the reversed string.
4. If both are equal, return True.
5. Otherwise, return False.

### Python Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse = s[::-1]

        if s == reverse:
            return True
        else:
            return False



2. Integer to Roman

The goal of this problem is to convert an integer into its Roman numeral representation.

Approach

I stored the integer values and their corresponding Roman symbols from largest to smallest.

For each value, I check whether it can be subtracted from the given number. If it can, I add the corresponding Roman symbol to the result and subtract the value from the number.

This continues until the number becomes 0.

Python Code
class Solution(object):
    def intToRoman(self, num):


        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]


        result = ""


        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value


        return result
