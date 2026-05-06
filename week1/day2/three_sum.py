# Problem: 3Sum
# LeetCode: #15
# Difficulty: Medium
# Topic: Arrays / Two Pointers
# Pattern: Sort + Two Pointers, skip duplicates
# Time: O(n^2) | Space: O(1)
# Date: Day 2 of 90
# Status: Solved ✓ / revisit

from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1 , len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res


# Key insight: Sort first — this enables two pointers AND makes
# duplicate detection trivial (dupes are always adjacent).
# Fix one element with the outer loop, then use two pointers
# on the remaining subarray to find pairs that sum to its negative.
# Skip duplicates at BOTH levels — outer loop (on i) and inner
# loop (on l after a valid triplet) — otherwise you get repeat answers.
# Sorting costs O(n log n) but the two-pointer scan is O(n),
# giving O(n²) overall which is optimal for this problem.