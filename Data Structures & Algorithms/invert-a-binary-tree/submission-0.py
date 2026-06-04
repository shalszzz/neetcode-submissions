# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(current):

            if not current:
                return 
        
            temp=current.right
            current.right=current.left
            current.left=temp

            dfs(current.left)
            dfs(current.right)
            
        dfs(root)
        return root
            
        