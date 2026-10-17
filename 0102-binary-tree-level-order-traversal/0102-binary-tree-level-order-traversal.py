# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        else:
            a=deque([root])
            res=[]
            while a:
                n=len(a)
                lis=[]
                for i in range(n):
                    b=a.popleft()
                    lis.append(b.val)
                    if b.left:
                        a.append(b.left)
                    if b.right:
                        a.append(b.right)
                res.append(lis)
            return res

        