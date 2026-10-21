# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def sym(x,y):
            if x is None and y is None:
                return True
            elif x is None or y is None:
                return False
            if x.val!=y.val:
                return False
            else:
                return sym(x.left,y.right) and sym(x.right,y.left)
        if root is None:
            return True
        return sym(root.left,root.right)
        