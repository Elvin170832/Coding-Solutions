# Problem: 121. Best Time to Buy and Sell Stock
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Topic: Arrays, Greedy
#
# Approach:
# Track the minimum price seen so far.
# Calculate the profit from selling at each current price.
# Update the maximum profit whenever a better one is found.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
