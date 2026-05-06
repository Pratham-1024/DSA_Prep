# Problem: Best Time to Buy and Sell Stock
# LeetCode: #121
# Difficulty: Easy
# Topic: Array / Greedy
# Pattern: Track running minimum
# Time: O(n) | Space: O(1)
# Date: Day 1 of 90
# Status: Solved ✓ / review

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0 
        sell = buy + 1
        
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell = buy + 1
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
                sell += 1
        
        return max_profit
    


# Key insight: You never need to look back. Track the lowest price
# seen so far as your buy point. For every new price, either it's
# lower (update buy) or it's a potential sell — compute profit and
# update the max. A new low always resets buy because buying cheaper
# can only improve future profit, never hurt it.
# No need for nested loops — one pass, two pointers, O(n).