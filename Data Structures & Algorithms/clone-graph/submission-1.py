"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d={}
        def dfs(inner_node):
            if inner_node is None:
                return None
            if inner_node.val in d:
                return d[inner_node.val]

            curr = Node(val=inner_node.val)
            d[inner_node.val]=curr
            # if neighbors is not None:
            neighbors = [dfs(neigbor) for neigbor in inner_node.neighbors]
            curr.neighbors=neighbors
            
            return curr
        return dfs(node)
        