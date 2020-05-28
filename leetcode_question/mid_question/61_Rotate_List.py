"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if not head.next:
            return head.next

        # 完成闭环
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # 从头开始遍历这个环
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        #找到结尾的节点
        new_head = new_tail.next
        new_tail.next = None

        return new_head

    def write_2(self, head, k):
        if not head:
            return None
        if not head.next:
            return head

        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head


node_1 = ListNode(1)
node_2 = ListNode(2)
node_1.next = node_2
node_3 = ListNode(3)
node_2.next = node_3
node_4 = ListNode(4)
node_3.next = node_4
node_5 = ListNode(5)
node_4.next = node_5


test = Solution()
print(test.rotateRight(
    node_1, 3
).val)