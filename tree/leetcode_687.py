# 687. Longest Univalue Path

# [Try: Accepted= 396ms 18.2MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        max_edges = 0

        def dfs(node):
            nonlocal max_edges

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            max_edges = max(max_edges, left + right)
            return max(left, right)

        dfs(root)

        return max_edges

