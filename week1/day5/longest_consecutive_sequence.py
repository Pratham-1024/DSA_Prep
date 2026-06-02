# Problem: Longest Consecutive Sequence
# LeetCode: #128
# Difficulty: Medium
# Topic: Array / HashSet
# Pattern: HashSet + Sequence Start Detection
# Time: O(n) | Space: O(n) 
# Date: Day 5 of 90
# Status: Solved ✓ / resolve

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        

# Key insight: Convert array to a HashSet for O(1) lookups.
# Only start counting a sequence if (num - 1) is NOT in the set —
# this means num is the start of a new sequence.
# From each start, keep incrementing while consecutive numbers exist.
# Looks like O(n²) but each number is visited at most twice —
# once in the outer loop, once in the inner while → truly O(n).
# The "start detection" trick is what makes this optimal.
