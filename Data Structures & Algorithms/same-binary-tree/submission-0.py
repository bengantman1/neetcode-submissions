# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def dfs(pnode, qnode):
            nonlocal same
            if not (pnode or qnode):
                return
            if not pnode or not qnode:
                same = False
                return
            if pnode.val != qnode.val:
                same = False
                return
            dfs(pnode.left, qnode.left)
            dfs(pnode.right, qnode.right)

        dfs(p, q)
        return same
            