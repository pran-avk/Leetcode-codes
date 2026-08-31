# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        if len(a)<=2:
            return [-1,-1]
        else:
            sumi=float("inf")
            first=prev=None
            for i in range(1,len(a)-1):
                if ((a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1])):
                    if first is None:
                        first=i
                        prev=i
                    else:
                        sumi=min(sumi,i-prev)
                        prev=i
            if first==None or first==prev:
                return [-1,-1]
            maxi=prev-first
            return[sumi,maxi]
        