# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def god(self,head,prev):
        if head is None:
            return None
        if head.next == None:
            head.next = prev
            return head
        nxt = head.next
        head.next = prev
        prev = head
        return self.god(nxt,prev)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        return self.god(head,prev)