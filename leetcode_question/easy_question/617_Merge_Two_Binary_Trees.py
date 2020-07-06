"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 124ms 14.1MB
        return self.merge_tree(t1, t2)

    def merge_tree(self, t1, t2):
        if not t1 and not t2:
            return None

        t1_value = t1.val if t1 else 0
        t2_value = t2.val if t2 else 0
        new_node = TreeNode(t1_value + t2_value)
        new_node.left = self.merge_tree(t1.left, t2.left)
        new_node.right = self.merge_tree(t1.right, t2.right)

        return new_node