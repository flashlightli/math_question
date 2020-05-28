"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 44ms 3.7MB
        if head == None or head.next == None:
            return head

        temp, temp.next = ListNode(0), head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return temp.next


head = ListNode(1)
second = ListNode(2)
third = ListNode(2)
head.next = second
second.next = third

test = Solution()
print(test.deleteDuplicates(
    head
))