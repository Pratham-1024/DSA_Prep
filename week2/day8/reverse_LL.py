# Problem: Reverse Linked List
# LeetCode: #206
# Difficulty: Easy
# Topic: Linked list , Recursion
# Pattern: Iterative Pointer Reversal
# Time: O(n) | Space: O(1)
# Date: Day 8 of 90
# Status: Solved ✓ / review



# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = None , head
        while curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        

        # Recursive Approach 
        def reverseList(self, head):
            if not head or not head.next:
                return head
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return newHead
        

# Key insight: Use three pointers — prev, curr, nxt.
# At each step, save next node, reverse the current pointer,
# then advance both prev and curr forward.
# prev trails curr by one — when curr hits None,
# prev is sitting at the new head.
# Key order: save nxt FIRST before reversing, or you lose the list.
# Recursive approach works too but costs O(n) stack space.