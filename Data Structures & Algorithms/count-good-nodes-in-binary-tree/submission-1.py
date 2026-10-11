# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, max_so_far=float('-inf')) -> int:
            if root is None:
                return 0
            
            cur=1 if root.val >= max_so_far else 0
            currmax = max(root.val, max_so_far)
            return cur+dfs(root.left, currmax)+dfs(root.right, currmax)

        return dfs(root)
        