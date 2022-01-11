"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 92ms 23.8MB
        if not head or not head.next:
            return True

        first_half_end = self.find_first_end(head)
        second_half_start = self.reverse_list(first_half_end.next)

        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result


    def find_first_end(self, head):
        # 使用快慢指针 找到中间的节点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_list(self, head):
        previous, current = None, head
        while current:
            current.next, current, previous = previous, current.next, current

        return previous