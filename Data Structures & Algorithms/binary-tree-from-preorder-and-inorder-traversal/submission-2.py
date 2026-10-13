# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        q=deque(preorder)
        idxs={v:i for i,v in enumerate(inorder)}
        def dfs(l,r, pivot=None):
            # nonlocal l_global
            nonlocal q
            # print(f'l: {l}, r: {r}, q: {q}')
            if r-l<=0:
                return None
            
            elif r-l==1:
                q.remove(inorder[l])
                # if inor
                return TreeNode(val=inorder[l])
            

            
                
            # if pivot is None:
            
            pivot=q.popleft()
            # l_global+=1

            i_pivot = idxs[pivot]
            left=dfs(l, i_pivot)
            right=dfs(i_pivot+1, r)

            return TreeNode(val=pivot, left=left, right=right)

        return dfs(0,len(preorder))

