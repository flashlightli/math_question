"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        if not l2:
            return l1

        tmp = ListNode(1)
        result = ListNode(1)
        result.next = tmp
        while l1 and l2:
            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next

            tmp = tmp.next

        if not l1:
            tmp.next = l2

        if not l2:
            tmp.next = l1

        return result.next


