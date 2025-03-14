# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        # Checks the first one
        if head.val == val:
            head = head.next

        if not head:
            return head
            
        # Previous and current
        curr = head.next
        prev = head
        while curr:
            # Skips that value
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        
        # Checks the first one
        if head.val == val:
            head = head.next

        return head
        