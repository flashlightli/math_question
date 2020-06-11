"""
给定一个二叉树，原地将它展开为一个单链表。
例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 把左子树插入到根节点和右子树之间
        return self.to_right(node=root)

    def to_right(self, node):
        if not node:
            return

        self.to_right(node.left)
        self.to_right(node.right)
        if node.left:
            pre = node.left
            while pre.right:
                pre = pre.right
            pre.right = node.right
            node.right = node.left
            node.left = None

root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
root.right = TreeNode(2)
# root.right = TreeNode(5)
root.right.right = TreeNode(3)



test = Solution()
print(test.flatten(
    root
))