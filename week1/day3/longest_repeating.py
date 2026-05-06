# Problem: Longest Substring without Repeating Characters
# LeetCode: #3
# Difficulty: Medium
# # Topic: String / Sliding Window
# Pattern: Variable size sliding window + HashSet
# Time: O(n) | Space: O(n)
# Date: Day 3 of 90
# Status: Solved ✓ / review 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # Hashset Approach
        charSet = set()
        left = 0
        max_window = 0

        for right,char in enumerate(s):
            while char in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(char)
            window = right-left+1
            max_window = max(max_window,window)
        
        return max_window
    
    # Haspmap Approach (optimal)
        charMap = {}
        left = 0
        max_window = 0

        for right, char in enumerate(s):
            if char in charMap and charMap[char] >= left:
                left = charMap[char] + 1
            charMap[char] = right
            max_window = max(max_window, right - left + 1)

        return max_window
    

# Key insight: Use a sliding window to track the current substring.
# Expand right freely — when a duplicate is found, shrink from
# the left until the duplicate is removed, then continue expanding.
# A set gives O(1) lookup to detect duplicates instantly.
# At every step, window size = right - left + 1, track the max.
# Every character is added and removed at most once → O(n) overall.