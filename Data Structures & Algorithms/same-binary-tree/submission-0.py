# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p and q) or (p and not q):
                # I.e one of the node is null => tree is not same
                return False

            if not p and not q:
                return True

            if p.val != q.val:
                return False

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            return True and (left and right)


        return dfs(p, q)
        