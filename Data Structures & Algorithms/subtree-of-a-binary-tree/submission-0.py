# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def bfs(t1,t2):
            q=deque([(t1,t2)])

            while q:
                m,n=q.popleft()

                if not m and not n:
                    continue
                
                if not m or not n:
                    return False

                if m.val!=n.val:
                    return False

                q.append((m.left, n.left))
                q.append((m.right, n.right))

            return True

        q=deque([root])

        while q:
            curr=q.popleft()

            if not curr:
                continue

            if curr.val==subRoot.val:
                if bfs(curr,subRoot):
                    return True

            q.append(curr.left)
            q.append(curr.right)
        
        return False


            
        