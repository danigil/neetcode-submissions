# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret=None
        c=0

        def dfs(curr: Optional[TreeNode]):
            nonlocal c, ret
            if curr and not ret:
                dfs(curr.left)
                c+=1
                if c==k:
                    ret=curr.val
                    return
                dfs(curr.right)

        dfs(root)
        
        return ret

        