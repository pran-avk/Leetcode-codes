# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        a=0
        while head:
            a=a*10+head.val
            head=head.next
        s=0
        c=0
        while a:
            b=a%10
            if b==1:
                c+=2**s
                s+=1
            else:
                s+=1
            a=a//10
        return c

        