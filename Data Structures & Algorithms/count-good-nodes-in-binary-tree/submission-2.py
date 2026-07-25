class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, rootVal):
            if not root:
                return 0 

            if root.val >= rootVal:
                res = 1
                rootVal = max(root.val, rootVal)
            else:
                res = 0
                # rootVal stays the same — this node didn't raise the max

            res += dfs(root.left, rootVal)
            res += dfs(root.right, rootVal)

            return res 

        return dfs(root, root.val)