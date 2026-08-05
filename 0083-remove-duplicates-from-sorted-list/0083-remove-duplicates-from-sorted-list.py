# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        a=head
        while a and a.next:
            b=a.next
            if a.val==b.val:
                a.next=a.next.next
            else:
                a=a.next
        return head        