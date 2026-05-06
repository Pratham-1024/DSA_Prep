# Problem: Valid Anagram
# LeetCode: #242
# Difficulty: Easy
# Topic: string / HashTable
# Pattern: Frequency Count / Hashmap
# Time: O(s+t) | O(s+t)
# Date: Day 2 of 90
# Status: Solved ✓ / review



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    

        # One Hashmap optimization
        # count = {}
        # for i in range(len(s)):
        #     count[s[i]] = count.get(s[i], 0) + 1
        #     count[t[i]] = count.get(t[i], 0) - 1
        # return all(v == 0 for v in count.values())

        # one-liner
        # return counter(s) == counter(t)
        # Sorting
        # return sorted(s) == sorted(t)
        

# Key insight: Two strings are anagrams if every character appears
# the same number of times in both. Build a frequency map for each
# and compare — if they're equal, it's an anagram.
# Optimization: use a single map, increment for s and decrement for t.
# If all values cancel to 0, the strings are anagrams.
# Early length check avoids unnecessary work.