# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            head = None
        llen = 0
        c = head
        while not (c == None):
            llen += 1
            c = c.next
        print(llen)
        count = 0
        curr = head
        prev = None
        while not (curr == None):
            if llen - n == 0:
                head = head.next
                return head
            if count == llen - n:
                if prev is not None:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            prev = curr
            curr = curr.next
            count += 1
        return head
            