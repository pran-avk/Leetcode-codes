# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def leng(root):
            if root is None:
                return 0
            else:
                a=leng(root.left)
                b=leng(root.right)
                return max(a,b)+1
        return leng(root)
        