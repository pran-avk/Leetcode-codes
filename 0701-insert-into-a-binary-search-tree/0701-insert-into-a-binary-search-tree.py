# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        def tree(root):
            if root is None:
                return TreeNode(val)
            elif root.val>val:
                root.left=tree(root.left)
            else :
                root.right=tree(root.right)
            return root
        return tree(root)
        