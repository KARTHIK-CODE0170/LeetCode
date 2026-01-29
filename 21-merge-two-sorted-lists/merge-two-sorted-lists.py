# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(-1)
        tail = res
        while(list1 != None and list2 != None):
            ans = None
            if(list1.val <= list2.val):
                ans = list1
                list1 = list1.next
            else:
                ans = list2
                list2 = list2.next
            tail.next = ans
            tail = tail.next                
        if(list1):
            tail.next = list1
        else:
            tail.next = list2
        return res.next
