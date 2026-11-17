# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(root,a):
            if root is None:
                return False
            if not root.left and not root.right:
                return a+root.val==targetSum
            c=dfs(root.left,a+root.val)
            b=dfs(root.right,a+root.val)
            return c or b
        return dfs(root,0)