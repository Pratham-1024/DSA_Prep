# Problem: Subarray Sum Equals K
# LeetCode: #560
# Difficulty: Medium
# Topic: Array / Prefix Sum / HashMap
# Pattern:  Prefix Sum + HashMap
# Time: O(n) | Space: O(n)
# Date: Day 4 of 90
# Status: Solved ✓ / resolve


from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res
    
    
    
# Key insight: Instead of checking every subarray (O(n²)),
# use a running prefix sum. If curSum - k exists in the map,
# it means there's a subarray ending here that sums to k.
# Store each prefix sum's frequency in a HashMap as you go.
# Seed the map with {0: 1} to handle subarrays starting at index 0.
# The difference (curSum - k) is the "complement" trick —
# same idea as Two Sum but applied to subarray sums.