"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        # 32ms  14MB  list缓存每层的节点
        if not root:
            return []

        result = []
        temp = [root]
        while temp:
            next_row = []
            row_result = []
            for item in temp:
                if not item:
                    continue
                row_result.append(item.val)
                next_row.append(item.left)
                next_row.append(item.right)
            temp = next_row
            if row_result:
                result.append(row_result)

        return result
