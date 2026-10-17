# Problem: 53. Maximum Subarray
# LeetCode: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Topic: Arrays, Dynamic Programming, Kadane's Algorithm
#
# Approach:
# Maintain a running sum of the current subarray.
# Update the maximum sum whenever a larger sum is found.
# Reset the running sum if it becomes negative.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            if total > max_sum:
                max_sum = total

            if total < 0:
                total = 0

        return max_sum
