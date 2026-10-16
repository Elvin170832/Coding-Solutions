# Problem: 136. Single Number
# LeetCode: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Topic: Arrays, Brute Force
#
# Approach:
# For each element, count how many times it appears
# in the entire array. Return the element that appears once.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for target in nums:
            count = 0

            for num in nums:
                if target == num:
                    count += 1

            if count == 1:
                return target
