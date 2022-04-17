class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode):
        # 如果 当前节点等于目标节点 那么后继节点为当前节点的右子树的最左节点或者为当前节点的父节点
        def get_left_node(node):
            # 右子树的最左节点
            if not node:
                return None

            curr = node
            while curr:
                if curr.left:
                    curr = curr.left
                else:
                    break
            return curr

        def get_node(node):
            if not node:
                return None

            result = None
            if node.val == p.val:
                result = get_left_node(node.right)
            if not result and node.val < p.val:
                result = get_node(node.right)
            if not result and node.val > p.val:
                # 当前节点的父节点
                result = get_node(node.left) or node

            return result

        return get_node(root)