# Problem: 217. Contains Duplicate
# LeetCode: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Topic: Arrays, Hash Set
#
# Approach:
# Store each number in a set.
# If a number is already in the set, return True.
# If no duplicates are found, return False.
#
# Time Complexity: O(n) average
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
