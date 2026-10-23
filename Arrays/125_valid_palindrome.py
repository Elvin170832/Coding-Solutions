# Problem: 125. Valid Palindrome
# LeetCode: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Topic: Strings, String Reversal
#
# Approach:
# Create an empty string to store the cleaned characters.
# Keep only letters and numbers using isalnum().
# Convert each valid character to lowercase and concatenate it.
# Reverse the cleaned string using [::-1].
# Compare the cleaned string with its reverse.
# If both strings are equal, return True; otherwise, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat_s = ""

        for char in s:
            if char.isalnum():
                concat_s += char.lower()

        if concat_s == concat_s[::-1]:
            return True
        else:
            return False
