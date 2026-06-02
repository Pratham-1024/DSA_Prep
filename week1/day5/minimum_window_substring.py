# Problem: Minimum Window Substring
# LeetCode: #76
# Difficulty: Hard
# Topic: HashMap / string / Sliding window
# Pattern: Variable Sliding Window + Dual HashMap
# Time: O(n + m) | Space: O(n + m)
# Date: Day 5 of 90
# Status: Solved ✓ / resolve


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        

# Key insight: Use two HashMaps — one for required chars (countT),
# one for the current window. Track "have" (chars meeting requirement)
# vs "need" (total unique chars required).
# Expand right freely, adding chars to window map.
# Only increment "have" when window[c] exactly equals countT[c] —
# extra copies don't count.
# When have == need, a valid window is found — record it, then
# shrink from left to find a smaller valid window.
# Decrement "have" only when window drops below required count.
# Result: one pass O(n), each char added/removed at most once.