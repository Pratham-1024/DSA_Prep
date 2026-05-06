# Problem: Contains Duplicate
# LeetCode: #217
# Difficulty: Easy
# Topic: Array / HashSet
# Pattern: HashSet Membership check
# Time: O(n) | Space: O(n)
# Date: Day 2 of 90
# Status: Solved ✓ / review


from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        s = set()

        for i in nums:
            if i in s:
                return True
            s.add(i)
        
        return False 

        # if len(s) != len(nums):
        #     return True
        # else:
        #     return False

        # one liner -> return len(set(nums)) != len(nums)
        

# Key insight: A set only stores unique elements — so if the set is
# smaller than the original array, a duplicate must exist.
# Better yet, check membership before inserting: the moment you try
# to add a number that's already in the set, you can return True
# immediately without processing the rest of the array.