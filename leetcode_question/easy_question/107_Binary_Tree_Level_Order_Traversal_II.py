"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        # 48ms 14.5MB
        # 最后翻转一下就好
        if not root:
            return []

        result = []
        tmp_node = [root]
        while tmp_node:
            tmp, node_list = [], []
            for node in tmp_node:
                tmp.append(node.val)
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)

            result.append([tmp])
            tmp_node = node_list

        return result.reverse()
