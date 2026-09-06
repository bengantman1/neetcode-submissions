# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        iterations = length // k
        prev = None
        cur = head
        res = None
        iteration = 0
        prevTail = head
        for iteration in range(iterations):
            prev = None
            segmentHead = cur
            i = 0
            while i < k:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                i += 1
            if iteration == 0:
                res = prev
            else:
                prevTail.next = prev # set previous tail to beginning of next
                prevTail = segmentHead
            iteration += 1
        prevTail.next = cur
        return res
        