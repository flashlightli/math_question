class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_loop(root):
    # 前序遍历
    result = []
    if not root:
        return result

    result.append(root.val)
