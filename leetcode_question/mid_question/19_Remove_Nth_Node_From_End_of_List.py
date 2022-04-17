# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 本质是快慢指针
        Tmp = ListNode()
        last_target, target = None, None
        index = 0
        start = Tmp
        start.next = head
        while start.next:
            if index < n:
                last_target, target = Tmp, head
            else:
                last_target, target = target, target.next
            start = start.next
            index += 1 if start else 0
            print("===")

        last_target.next = target.next if n >= 2 else None
        return Tmp.next


def get_list_node(list_demo):
    head = ListNode()
    curr = head
    for index, value in enumerate(list_demo):
        tmp = ListNode(value)
        curr.next = tmp
        curr = curr.next

    return head.next


test = Solution()
print(test.removeNthFromEnd(
    get_list_node([1, 2, 3, 4, 5]), 2
))