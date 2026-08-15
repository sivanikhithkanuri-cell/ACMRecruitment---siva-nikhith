# Greedy Algorithms

This folder contains my solutions for the Greedy Algorithms challenge.

The two problems solved are:

1. Lemonade Change
2. Assign Cookies

Both problems were solved using Python.

---

## 1. Lemonade Change

### Approach

Each lemonade costs $5 and customers can pay using $5, $10, or $20 bills.

I keep track of the number of $5 and $10 bills available.

* If a customer gives $5, I keep the bill.
* If a customer gives $10, I give one $5 bill as change.
* If a customer gives $20, I first try to give $10 + $5 as change.
* If that is not possible, I try to give three $5 bills.
* If neither option is possible, I return `False`.

The greedy choice is to use a $10 and a $5 bill first when giving change for $20. This preserves more $5 bills for future customers.

### Python Solution

```python
class Solution(object):
    def lemonadeChange(self, bills):
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if five == 0:
                    return False

                five -= 1
                ten += 1

            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                elif five >= 3:
                    five -= 3

                else:
                    return False

        return True
```

### Complexity

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

---

## 2. Assign Cookies

### Approach

Each child has a greed factor representing the minimum cookie size required to satisfy that child.

I first sort both the greed factors and cookie sizes. Then I start with the least greedy child and the smallest cookie.

If the current cookie is large enough for the current child, I assign it and move to the next child. Otherwise, I try the next larger cookie.

The greedy choice is to give each child the smallest cookie that can satisfy them, preserving larger cookies for children with larger greed factors.

### Python Solution

```python
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child
```

### Complexity

* Time Complexity: `O(n log n + m log m)`
* Auxiliary Space Complexity: `O(1)`, excluding the internal space used by Python's sorting implementation.

---

## Submission Files

This folder also contains:

* Accepted LeetCode submission screenshot for Lemonade Change
* Accepted LeetCode submission screenshot for Assign Cookies
* Handwritten algorithm explanation for both problems

