# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def height(n):
            if n is None:
                return 0

            height(n.left)
            height(n.right)

            self.maxDiameter = max(self.maxDiameter, height(n.left) + height(n.right))

            return max(height(n.left), height(n.right)) + 1
        height(root)
        return self.maxDiameter
