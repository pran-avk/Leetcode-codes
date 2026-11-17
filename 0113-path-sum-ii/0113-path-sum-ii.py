
class Solution(object):
    def pathSum(self, root, targetSum):
        result = []
        path = []

        def dfs(root, total):
            if root is None:
                return

            path.append(root.val)
            total += root.val

            if not root.left and not root.right:
                if total == targetSum:
                    result.append(path[:])
            else:
                dfs(root.left, total)
                dfs(root.right, total)

            path.pop()

        dfs(root, 0)
        return result
