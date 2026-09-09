# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and  head.val==val:
            head=head.next
        head1=head
        while head1 and head1.next:
            if head1.next.val==val:
                head1.next=head1.next.next
            else:
                head1=head1.next
        return head
        