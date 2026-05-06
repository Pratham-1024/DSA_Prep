# Problem: Two Sum
# LeetCode: #1
# Difficulty: Easy
# Topic: Hashmap
# Pattern: Hashmap , one pass 
# Time: O(n) | Space: O(n)
# Date: Day 1 of 90
# Status: Solved ✓ / revisit

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        twosum = {}

        for index, num in enumerate(nums):
            diff = target - num 

            if diff in twosum:
                return [twosum[diff], index]

            twosum[num] = index 
        
        
# Key insight: Instead of checking every pair (brute O(n²)),
# store each number's index in a hashmap as you go.
# For each new number, check if its complement (target - num)
# already exists in the map — if yes, you've found your pair.
# The "one pass" trick works because by the time you need
# a complement, it's either already stored or will be found later.
# Trade space (O(n) hashmap) to drop time from O(n²) → O(n).