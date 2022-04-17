class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_value = 0
    max_single_value = 0

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_single_value = root.val

        def recursion_node(node):
            if not node:
                return 0
            self.max_single_value = max(self.max_single_value, node.val)
            left_value, right_value = 0, 0
            if node.left:
                left_value = recursion_node(node.left)
            if node.right:
                right_value = recursion_node(node.right)

            self.max_value = max(left_value, right_value, right_value + node.val, left_value + node.val + right_value,
                                 node.val, 0, self.max_value)
            return max(left_value + node.val, right_value + node.val, 0, node.val)

        recursion_node(root)
        return self.max_value if self.max_single_value >= 0 else self.max_single_value