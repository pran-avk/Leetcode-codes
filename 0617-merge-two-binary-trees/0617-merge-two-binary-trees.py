# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        def tre(root1,root2):
            if root1 is None:
                return root2
            if root2 is None:
                return root1
            root1.val+=root2.val
            root1.right=tre(root1.right,root2.right)
            root1.left=tre(root1.left,root2.left)
            return root1
        return tre(root1,root2)
        
        