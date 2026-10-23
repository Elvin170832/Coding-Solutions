# Problem: 242. Valid Anagram
# LeetCode: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Topic: Strings, Character Frequency Counting
#
# Approach:
# 1. If the strings have different lengths, return False.
# 2. Count each character in both strings using count().
# 3. If any character has different frequencies, return False.
# 4. If all frequencies match, return True.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if s.count(char) != t.count(char):
                return False

        return True
