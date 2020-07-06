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


def sort_dict(dict_test):
    demo = sorted(dict_test.items(), key=lambda x: x[1], reverse=True)
    return demo

demo = {'a': 1, 'b': 0, 'c': -3, 'd': 3}

print(sort_dict(demo))


def get_child2(dict_test, target):
    result = []
    tmp_dict = {}
    for key, value in dict_test.items():
        tmp_dict[value] = (tmp_dict[value] + [key]) if value in tmp_dict else [key]

    tmp = tmp_dict.get(target, [])
    result.extend(tmp)
    while tmp:
        tmp_list = tmp_dict.get(tmp.pop(), [])
        result.extend(tmp_list)
        tmp += tmp_list
        tmp = list(set(tmp))

    return result


demo2_dict = {1: 2, 2: 3, 4: 3, 5: 3, 6: 5}
print(get_child2(demo2_dict, 3))