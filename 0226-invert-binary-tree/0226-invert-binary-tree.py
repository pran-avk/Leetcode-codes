# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def xyz(root):
            if root is None:
                return
            root.left,root.right=root.right,root.left
            xyz(root.right)
            xyz(root.left)
            return root
        return xyz(root)
        