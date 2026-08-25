# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        res = ListNode(0, None)
        head = res
        while a or b:
            if not a:
                res.next = b
                return head.next
            elif not b:
                res.next = a
                return head.next
            elif a.val < b.val:
                res.next = a
                a = a.next
            else:
                res.next = b
                b = b.next
            res = res.next
        return head.next

