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
            return 
        
        mystack=[node]
        clones={node: Node(node.val)}


        def dfs(node):
            while mystack:
                top=mystack.pop()

                for nei in top.neighbors:
                    if nei not in clones:
                        clones[nei]=Node(nei.val)
                        mystack.append(nei)
                        
                    clones[top].neighbors.append(clones[nei])
                    
            return clones[node]
        return dfs(node)
                  
                    