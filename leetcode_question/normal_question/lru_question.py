"""
最近最少使用算法
"""


class LRUCache(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.items = {}  # 存节点的键值对，方便查找某节点是否存在链表中
        self.head = self.Node(-1, -1)  # 双向链表头初始化
        self.tail = self.Node(-1, -1)  # 双向链表尾初始化
        self.head.next = self.tail  # 将头与尾连接起来
        self.tail.prev = self.head

    def __remove(self, node):
        """remove node.
        :params node: remove this node
        """
        node.prev.next = node.next  # 当前节点的前节点的next指向当前节点的后节点
        node.next.prev = node.prev  # 当前节点的后节点的prev指向当前节点的前节点
        node.prev = None  # 把当前节点的前节点置空
        node.next = None

    def __insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.items:
            return -1
        node = self.items[key]
        self.__remove(node)  # 先删除该节点，然后在表头重新接入
        self.__insert(node)
        return node.value

    def put(self, key, value):
        if key in self.items:
            node = self.items[key]
            self.__remove(node)
            node.value = value
            self.__insert(node)
        else:
            # 判断LRU缓存中是否已经达到最大容量，是的话就删除表尾节点，然后再执行插入操作
            if self.size == self.capacity:
                discard = self.tail.prev
                self.__remove(discard)
                del self.items[discard.key]
                self.size -= 1

            node = self.Node(key, value)
            self.items[key] = node
            self.__insert(node)
            self.size += 1
