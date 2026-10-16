# Problem: 1295. Find Numbers with Even Number of Digits
# LeetCode: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Difficulty: Easy
# Topic: Arrays, Loops, Digit Counting
#
# Approach:
# Count the digits in each number using integer division.
# If the digit count is even, increment the result.
#
# Time Complexity: O(n * d)
# Space Complexity: O(1)
# where n = number of elements and d = maximum number of digits.

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        digits = 0

        for num in nums:
            count = 0

            while num > 0:
                count += 1
                num = num // 10

            if count % 2 == 0:
                digits += 1

        return digits
