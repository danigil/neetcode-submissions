# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def dfs(curr: Optional[TreeNode], level=0):
            if not curr:
                return

            dfs(curr.right, level+1)
            dfs(curr.left, level+1)

            nonlocal d
            if level not in d:
                d[level]=curr.val
        
        dfs(root)
        ret=[None]*len(d.keys())
        for k,v in d.items():
            ret[k]=v
        return ret

        