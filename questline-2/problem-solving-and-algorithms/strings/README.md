# String Algorithms

This folder contains solutions for two string problems from LeetCode.

## 1. Valid Palindrome

### Problem
Check whether a given string is a palindrome after removing spaces and special characters and converting uppercase letters to lowercase.

### Approach
1. Create an empty string called `cleaned`.
2. Go through every character in the given string.
3. Check whether the character is a letter or number using `isalnum()`.
4. Convert the character to lowercase and add it to `cleaned`.
5. Reverse the cleaned string.
6. Compare the original cleaned string with the reversed string.
7. If they are equal, return `True`. Otherwise, return `False`.

### Time Complexity
O(n)

### Space Complexity
O(n)

---

## 2. Zigzag Conversion

### Problem
Arrange the characters of a string in a zigzag pattern using the given number of rows and then read the characters row by row.

### Approach
1. Create empty strings for each row.
2. Start from the first row.
3. Add each character to the current row.
4. Move downward through the rows.
5. When the last row is reached, change direction and move upward.
6. When the first row is reached, change direction again.
7. Continue until all characters are added.
8. Join all the rows together and return the final string.

### Time Complexity
O(n)

### Space Complexity
O(n)
