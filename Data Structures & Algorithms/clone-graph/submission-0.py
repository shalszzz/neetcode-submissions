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
        
        mystack=[]
        mystack.append(node)
        cloned_nodes={node:Node(node.val)}

        def dfs(node):
            while mystack:
                curr=mystack.pop()
                
                for nei in curr.neighbors:
                    if nei not in cloned_nodes:
                        cloned_nodes[nei]=Node(nei.val)
                        mystack.append(nei)

                    cloned_nodes[curr].neighbors.append(cloned_nodes[nei])
            return cloned_nodes[node]

        return dfs(node)
                

        