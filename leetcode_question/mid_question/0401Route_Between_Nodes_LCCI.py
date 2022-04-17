class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    result = 0

    # 前缀和怎么应用呢？
    # 如果两个数的前缀总和是相同的，那么这些节点之间的元素总和为零。进一步扩展相同的想法，如果前缀总和currSum，在节点A和节点B处相差target，
    # 则位于节点A和节点B之间的元素之和是target。

    def pathSum(self, root: TreeNode, sum: int) -> int:
        all_dic = {0: 1}
        # key是前缀和 value是出现次数

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            # 获取 当前的和 - 上面节点的值 = 目标值 所以能拿到目标值的和
            # 所以初始值赋值0:1
            ret += all_dic.get(curr - sum) or 0
            all_dic[curr] = (all_dic.get(curr) or 0) + 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            # 当前的值 - 1 ,确保all_dic的有效数据都是父级节点的
            all_dic[curr] -= 1
            return ret

        return dfs(root, 0)