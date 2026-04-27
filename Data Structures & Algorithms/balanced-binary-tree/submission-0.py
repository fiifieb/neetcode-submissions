# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node,height):
            if node.left and node.right:
                r = dfs(node.right, height + 1)
                l = dfs(node.left, height + 1)
                if r and l and abs(r-l)<2:
                    return max(r,l)
                else:
                    return False
            elif node.left:
                l = dfs(node.left, height + 1)
                if l and l - height < 2:
                    return l
                else:
                    return False
            elif node.right:
                r = dfs(node.right, height + 1)
                if r and r - height < 2:
                    return r
                else:
                    return False
            else:
                return height

        return bool(dfs(root,1))