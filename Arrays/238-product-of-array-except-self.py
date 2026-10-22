```python
# Problem: 238. Product of Array Except Self
# LeetCode: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Topic: Arrays, Prefix Sum, Suffix Product
#
# Approach:
# Use prefix and suffix products to calculate the product
# of all elements except the current element.
# In the first pass, store the product of all elements to the left.
# In the second pass, multiply each result by the product
# of all elements to the right.
# Avoid division and use only constant extra space.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding the output array)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
```
