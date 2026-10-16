# Problem: 283. Move Zeroes
# LeetCode: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Topic: Arrays
#
# Approach:
# Find a zero and search for the next non-zero element.
# Swap them, then continue searching.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
