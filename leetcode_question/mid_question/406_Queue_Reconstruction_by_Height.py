"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reconstructQueue(self, people):
        # 高的人不会受低的人影响，所以优先处理高的人，排序完后，按从高到低和优先级处理，先处理高的并且序号小的，序号便是插入的位置
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i in people:
            res.insert(i[1], i)
        return res


test = Solution()
print(test.reconstructQueue(
    people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
))