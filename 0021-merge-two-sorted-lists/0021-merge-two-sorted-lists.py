# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        a=ListNode(0)
        b=a
        while list1 and list2:
            if list1.val<list2.val:
                b.next=list1
                list1=list1.next
            else:
                b.next=list2
                list2=list2.next
            b=b.next
        if list1:
            b.next=list1
        if list2:
            b.next=list2
        return a.next
        