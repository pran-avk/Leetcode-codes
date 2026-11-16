# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        a=head
        b=head
        count=0
        while a:
            count+=1
            a=a.next
        c=head
        if count==n:
            return head.next
        for i in range(count-n-1):
            c=c.next
        c.next=c.next.next
        return head

        