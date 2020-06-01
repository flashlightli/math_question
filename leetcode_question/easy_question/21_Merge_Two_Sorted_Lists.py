"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
"""
from leetcode_question.utils import show_list_node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 48ms 13.7MB
        # pre_head 是假的头节点
        pre_head = ListNode(-1)
        prev = pre_head

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1.val
                l1 = l1.next
            else:
                prev.next = l2.val
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return pre_head.next


test = Solution()
print(test.mergeTwoLists(
    "["
))
