# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x,y = list1,list2
        head = ListNode(-1)
        temp = head
        while x is not None and y is not None:
            ans = ListNode(-1)
            if x.val <= y.val:
                ans.val = x.val
                temp.next = ans
                x = x.next
                temp = temp.next
            else:
                ans.val = y.val
                temp.next = ans
                y = y.next
                temp = temp.next
        if x:
            temp.next = x
        if y:
            temp.next = y
        return head.next
            