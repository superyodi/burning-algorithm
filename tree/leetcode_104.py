# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.

# [Try: Accepted]	32 ms	16.4 MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        global max_depth
        max_depth = 0

        def dfs(node, depth):
            global max_depth

            if not node:
                max_depth = max(max_depth, depth)
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return max_depth




