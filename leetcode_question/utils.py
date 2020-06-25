class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


demo_dict = {"a": 1, "b": 3, "c": 2}
print(sorted(demo_dict.items(), key=lambda x: x[1]))
