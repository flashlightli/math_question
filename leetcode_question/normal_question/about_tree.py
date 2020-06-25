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


def post_order(root):
    result = []
    if not root:
        return result

    WHITE, GRAY = 0, 1
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if color == WHITE:
            stack.append((GRAY, node))
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
        else:
            result.append(node.val)

    return result


def mid_order(root):
    result = []
    if not root:
        return result

    WHITE, GRAY = 0, 1
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((GRAY, node))
            stack.append((WHITE, node.left))
        else:
            result.append(node.val)

    return result
