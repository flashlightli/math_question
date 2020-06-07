"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        # 76ms 15.9MB
        # 递归求子节点
        if not nums:
            return

        start_i, end_j = 0, len(nums)
        mid = (start_i + end_j) // 2
        root = TreeNode(0)
        root.val = nums[mid]
        root.left = self.sorted_bst(nums[:mid], root)
        root.right = self.sorted_bst(nums[mid + 1:], root)

        return root

    def sorted_bst(self, nums, node):
        if not nums:
            return
        if len(nums) == 1:
            tmp = TreeNode(0)
            tmp.val = nums[0]
            return tmp

        start_i, end_j = 0, len(nums)
        mid = (start_i + end_j) // 2
        tmp_node = TreeNode(nums[mid])
        print(nums[:mid], nums[mid+1:])
        tmp_node.left = self.sorted_bst(nums[:mid], tmp_node)
        tmp_node.right = self.sorted_bst(nums[mid + 1:], tmp_node)

        return tmp_node

test = Solution()
print(test.sortedArrayToBST(
    [3, 5, 8]
))