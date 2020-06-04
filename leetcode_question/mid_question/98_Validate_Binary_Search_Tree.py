"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 60ms 16.1MB
        # 递归  注意 根节点的处理以及节点值是0的处理
        if not root:
            return True

        return self.vaild_tree(root.left, left_val=None, right_val=root.val) and \
               self.vaild_tree(root.right, left_val=root.val, right_val=None)

    def vaild_tree(self, root, left_val=None, right_val=None):
        if not root:
            return True

        if (left_val != None and root.val <= left_val) or (right_val != None and root.val >= right_val):
            return False

        return self.vaild_tree(root.left, left_val, root.val) and \
               self.vaild_tree(root.right, root.val, right_val)


root = TreeNode(0)
# left = TreeNode(1)
right = TreeNode(-1)
# root.left = left
root.right = right


test = Solution()
print(test.isValidBST(
    root
))