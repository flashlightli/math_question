class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def show_list_node(head):
    if not head:
        return head

    while head:
        print(head.val)
        head = head.next