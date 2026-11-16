# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        b=ListNode(0)
        a.sort()
        c=b
        for i in range(len(a)):
            c.next=ListNode(a[i])
            c=c.next
        return b.next

        