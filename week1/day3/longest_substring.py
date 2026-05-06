# Problem: Longest Repeating Charcter Replacement
# LeetCode: #424
# Difficulty: Medium
# Topic: String / Sliding Window
# Pattern: Variable size sliding window + frequency map
# Time: O(n) | Space: O(1)  # at most 26 keys in the map
# Date: Day 3 of 90
# Status: Solved ✓ / resolve 


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        # maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # maxf = max(maxf, count[s[r]])

            # Max Frequency Optimization can be done by replacing max(count.values) to maxf 

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
        

# Key insight: A window is valid if (window size - most frequent char count) <= k
# because you only need to replace the non-dominant characters.
# Expand right freely, shrink left when replacements needed exceed k.
# Track max frequency with maxf — it only ever needs to grow,
# because a smaller maxf can't produce a longer valid window than
# what we've already seen. O(1) space since charset is fixed (26 letters).