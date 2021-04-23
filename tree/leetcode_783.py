# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:
        min_gap = 10 ** 5
        pre_num = -1

        def inorder(node):
            nonlocal min_gap, pre_num

            if not node:
                return

            if node.left:
                inorder(node.left)

            if pre_num != -1:
                min_gap = min(min_gap, abs(node.val - pre_num))

            pre_num = node.val

            if node.right:
                inorder(node.right)

        inorder(root)

        return min_gap