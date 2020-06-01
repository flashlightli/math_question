"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 56ms 16.7
        # 两个循环 一个快 一个慢 看节点是否有一样的
        if not head or not head.next:
            return False

        first_cycle, second_cycle = head, head.next
        while first_cycle and second_cycle:
            if not first_cycle or not second_cycle:
                return False

            if first_cycle == second_cycle:
                return True

            first_cycle = first_cycle.next
            if second_cycle.next and second_cycle.next.next:
                second_cycle = second_cycle.next.next
            else:
                return False

        return False


head = ListNode(1)
second = ListNode(2)
third = ListNode(2)
head.next = second
second.next = third
third.next = head


test = Solution()
print(test.hasCycle(
    head
))



