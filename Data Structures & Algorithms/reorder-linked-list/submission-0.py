# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        cur = head

        reverseIdx = 0
        length = 0
        while cur:
            cur = cur.next
            length += 1
        reverseIdx = math.ceil(length / 2)
        i = 0
        cur = head
        prev = None
        while i < reverseIdx:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = None
        prev = None
        i = 0
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # prev is now head of reversed list
        # merge them
        cura = head
        a = 0
        curb = prev
        b = 0
        res = ListNode()
        newHead = res
        while cura or curb:
            if not cura:
                res.next = curb
                break
            if not curb:
                res.next = cura
                break
            if a > b:
                res.next = curb
                curb = curb.next
                b += 1
            else:
                res.next = cura
                cura = cura.next
                a += 1
            res = res.next

        head = newHead.next
            



        
