# Linked list templates — read before solving
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


        head = ListNode()
        # REVERSAL — 3 pointer technique
        prev, curr = None, head
        while curr:
            nxt = curr.next   # 1. save next
            curr.next = prev  # 2. reverse pointer
            prev = curr       # 3. advance prev
            curr = nxt        # 4. advance curr
        return prev           # prev is new head

        # DUMMY HEAD — use for merge/insert problems
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        # ... manipulate ...
        return dummy.next

        # FAST/SLOW — cycle + middle problems
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is at middle when fast reaches end