# Problem: Product Array Except Self
# LeetCode: #238
# Difficulty: Medium
# Topic: Array / Prefix Sum
# Pattern: Prefix Product + Suffix Product
# Time: O(n) | Space: O(n)
# Date: Day 4 of 90
# Status: Solved ✓ / revisit 


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        pre = [1]*n
        suf = [1]*n

        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1]*nums[i+1]

        for i in range(n):
            answer[i] = pre[i]*suf[i]

        return answer
    
        # optimization
        n = len(nums)
        answer = [1] * n

        # Build prefix directly into answer
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        # Multiply suffix on the fly
        suf = 1
        for i in range(n-2, -1, -1):
            suf *= nums[i+1]
            answer[i] *= suf

        return answer
                

# Key insight: For each index i, the answer is the product of
# everything to its LEFT multiplied by everything to its RIGHT.
# Build a prefix array (product of all elements before i) and
# a suffix array (product of all elements after i), then multiply them.
# No division needed — avoids the zero-element edge case entirely.
# O(1) space optimization: store prefix in the output array directly,
# then do a single reverse pass with a running suffix variable.