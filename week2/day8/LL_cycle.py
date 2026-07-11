# Problem: Linked List Cycle
# LeetCode: #141
# Difficulty: Easy
# Topic: Linked list / Two Pointer
# Pattern: Fast & Slow Pointers (Floyd's Cycle Detection)
# Time: O(n) | Space: O(1)
# Date: Day 8 of 90
# Status: Solved ✓ / review



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head ,  head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            
        return False
        
# Key insight: Use two pointers — slow moves 1 step, fast moves 2.
# If no cycle exists, fast hits None and we return False.
# If a cycle exists, fast laps slow inside the cycle —
# they're guaranteed to meet because fast gains exactly 1 step
# per iteration, so it can never skip over slow.
# O(1) space vs HashSet approach which costs O(n).
# Floyd's algorithm: meeting point proves cycle, no extra memory needed.