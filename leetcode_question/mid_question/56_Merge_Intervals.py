"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def merge(self, intervals):
        # 44ms 14.7MB
        # 重点 new_intervals = sorted(intervals, key=lambda x:x[0]) 根据item的第一个元素排序
        if not intervals:
            return []

        new_intervals = sorted(intervals, key=lambda x:x[0])
        result = [new_intervals[0]]
        for index, value in enumerate(new_intervals[1:]):
            compare_list = result[-1]
            if value[0] <= compare_list[1]:
                result[-1] = [compare_list[0], max(value[1], compare_list[1])]
            else:
                result.append(value)

        return result


test = Solution()
print(test.merge(
    [[1,4],[4,5]]
))