# Problem: Merge Two Sorted Lists 
# LeetCode: #21
# Difficulty: Easy
# Topic: Linked list , Recursion
# Pattern: Dummy Node + Two Pointer Merge
# Time: O(n + m) | Space: O(1)
# Date: Day 8 of 90
# Status: Solved ✓ / revisit


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional      
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next
    
        # Recursive Approach 
        def mergeTwoLists(self, list1, list2):
            if not list1: return list2
            if not list2: return list1
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
        

# Key insight: Use a dummy head node to avoid edge case handling
# for the result list's head — dummy.next is always the answer.
# Two pointers walk both lists simultaneously, always picking
# the smaller value and advancing that list forward.
# When one list is exhausted, attach the remainder of the other —
# no need to loop since it's already sorted.
# Dummy node pattern is reusable across many linked list problems.