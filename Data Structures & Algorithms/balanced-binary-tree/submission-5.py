# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.res = True 

        # Returns height
        def dfs(curr):
            if not curr:
                return 0


            left = dfs(curr.left)
            right = dfs(curr.right)

            diff = abs(left - right)
            self.res = self.res and diff <= 1

            return 1 + max(left, right)

        dfs(root)
        return self.res