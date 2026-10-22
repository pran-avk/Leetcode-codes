# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def tree(nums):
            if not nums: return None
            a=len(nums)
            mid=a//2
            root=TreeNode(nums[mid])
            root.left=tree(nums[:mid])
            root.right=tree(nums[mid+1:])
            return root
        return tree(nums)
        