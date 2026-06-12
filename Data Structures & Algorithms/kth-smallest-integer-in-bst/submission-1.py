# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.answer=None
        self.k=k

        def dfs(current):
            if not current:
                return 
            
            dfs(current.left)

            self.k-=1
            if self.k==0:
                self.answer=current.val
                return

            dfs(current.right)

        dfs(root)
        return self.answer

            
      

        



        