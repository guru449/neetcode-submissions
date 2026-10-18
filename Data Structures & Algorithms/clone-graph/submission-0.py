"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        hm = {}
        def dfs(nodeCopy):
            if nodeCopy == None:
                return None
            if nodeCopy in hm:
                return hm[nodeCopy]
            resultNode = Node(nodeCopy.val)
            hm[nodeCopy] = resultNode 
            for newNode in nodeCopy.neighbors:
                resultNode.neighbors.append(dfs(newNode))
            return resultNode

        return dfs(node)

        