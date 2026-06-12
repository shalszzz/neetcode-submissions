# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values=[]

        def dfs(current):
            if not current:
                return 
            self.values.append(current.val)
            dfs(current.left)
            dfs(current.right)
        
        dfs(root)
      

        self.myHeap= self.values
        heapq.heapify(self.myHeap)

        for i in range(k-1):
            heapq.heappop(self.myHeap)
        return self.myHeap[0]



        