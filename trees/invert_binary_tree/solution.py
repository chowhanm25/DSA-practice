# LeetCode 226: Invert Binary Tree
# Time: O(n) | Extra space: O(h), where h is the tree height.

class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        saved = root.left
        root.left = root.right
        root.right = saved

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
