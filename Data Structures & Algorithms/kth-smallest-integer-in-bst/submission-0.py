# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l=self.count(root.left)
        r=self.count(root.right)
        s=1+l+r

        root.count=s

        return s

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        self.count(root)
        
        def dfs(curr: Optional[TreeNode], k: int) -> int:
            l=curr.left.count if curr.left else 0

            if k==l+1:
                return curr.val
            elif k>l+1:
                return dfs(curr.right, k-l-1)
            else:
                return dfs(curr.left, k)



        return dfs(root,k)
        