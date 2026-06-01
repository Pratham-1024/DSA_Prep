# Problem: Group Anagrams
# LeetCode: #49
# Difficulty: Medium
# Topic: Array / HashMap / string / sorting
# Pattern: HashMap + Sorting / Frequency Key
# Time: O(n.mlogm) | Space: O(n.m)
# Date: Day 4 of 90
# Status: Solved ✓ / resolve


from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
        # optimization 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
                

# Key insight: Anagrams share the same sorted string — use it as
# a HashMap key to group them together in one pass.
# All strings that sort to the same characters belong to the same group.
# Optimization: replace sorted string with a 26-element frequency
# tuple as the key — avoids O(m log m) sort, brings it down to O(m).
# defaultdict(list) auto-initializes empty lists, keeping code clean.