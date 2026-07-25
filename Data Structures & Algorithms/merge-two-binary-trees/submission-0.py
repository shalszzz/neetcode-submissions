# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root1, root2):
            if not root1 and not root2:
                return None

            if root1 and root2:
                node = TreeNode(root1.val + root2.val)
            elif root1:
                node = TreeNode(root1.val)
            else:
                node = TreeNode(root2.val)

            node.left = dfs(root1.left if root1 else None,
                            root2.left if root2 else None)
            node.right = dfs(root1.right if root1 else None,
                             root2.right if root2 else None)

            return node

        return dfs(root1, root2)