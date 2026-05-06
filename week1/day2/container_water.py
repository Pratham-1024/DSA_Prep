# Problem: Container with Most Water
# LeetCode: #11
# Difficulty: Medium
# Topic: Array / Greedy
# Pattern: Two Pointer
# Time: O(n) | Space: O(1)
# Date: Day 2 of 90
# Status: Solved ✓ / revisit


from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left , right = 0 , len(height)-1

        while left < right:
            area = (right-left)*min(height[left],height[right])
            max_area = max(max_area,area)

            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return max_area 
    

# Key insight: Start with the widest possible container (left=0, right=end).
# Width can only shrink as pointers move inward, so to have any chance
# of increasing area, you MUST increase height.
# Always move the pointer with the shorter bar — keeping the taller one
# is the only way a future container could beat the current max.
# Moving the taller side guarantees a smaller area (shorter width, same
# or worse height), so it's never worth doing.
# Greedy choice at every step → optimal solution in one pass.