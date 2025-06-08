# Last updated: 6/7/2025, 11:34:02 PM
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow_ref = head
        fast_ref = head
        while fast_ref and fast_ref.next:
            slow_ref = slow_ref.next
            fast_ref = fast_ref.next.next
            if slow_ref == fast_ref:
                return True
        return False