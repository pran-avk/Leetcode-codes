# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def sym(a1,a2):
            if not a1 and not a2:
                return True
            elif not a1 or not a2:
                return False
            elif a1.val!=a2.val:
                return False
            b=sym(a1.left,a2.right)
            c=sym(a1.right,a2.left)
            return b&c
        return sym(root.left,root.right)

        