# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        cnt = -1
        temp = head
        while(temp != None):
            temp = temp.next
            cnt += 1
        temp = head
        res = 0
        while(temp != None):
            res += temp.val * (2 ** cnt)
            cnt -= 1
            temp = temp.next
        return res