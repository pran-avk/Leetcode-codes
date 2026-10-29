# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        b=[]
        def tree(root):
            if root is None:
                return
            tree(root.left)
            b.append(root.val)
            if len(b)==k:
                return 
            
            tree(root.right)
        tree(root)
        return b[k-1]