class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def revert_list(head):
    # 翻转链表
    prev, curr = None, head
    while curr:
        # 当前节点 上一个节点 上一个节点的下一个节点
        curr, prev, prev.next = curr.next, curr, prev

    return prev


def swap_list(head):
    # 两两交换链表
    prev, prev.next = ListNode(-1), head
    while prev.next and prev.next.next:
        a = prev.next
        b = a.next
        # 上一个节点 做交换的两个节点
        prev.next, a.next, b.next = b, b.next, a
        prev = a

    return prev.next

