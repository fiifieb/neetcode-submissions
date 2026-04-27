# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, height):
        if node.left and node.right:
            l = self.dfs(node.left, height + 1)
            r = self.dfs(node.right, height + 1)
            return max(l,r)
        elif node.left:
            return self.dfs(node.left, height + 1)
        elif node.right:
            return self.dfs(node.right, height + 1)
        else:
            return height

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root, 1)