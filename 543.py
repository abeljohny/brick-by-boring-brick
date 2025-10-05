# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if left + right > self.diameter:
                self.diameter = left + right
            return 1 + (left if left > right else right)

        depth(root)
        return self.diameter


# print(Solution().diameterOfBinaryTree(TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))))
