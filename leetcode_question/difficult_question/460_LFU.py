"""
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

示例：

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 双hash表
# {"key": ("Node", "count")}
# {
#     "count": []     # key是次数 链表数组 每次插入头部
# }
# min_count = [] 数组

class LFUCache:
    # 用于记录最后使用时间的链表
    class Node:
        def __init__(self, key: int):
            self.prev = None
            self.next = None
            self.key = key

        def add(self, node):
            self.next = node
            node.prev = self

        def delete_self(self):
            if self.next is not None:
                self.next.prev = self.prev
            if self.prev is not None:
                self.prev.next = self.next

    # 用于记录使用次数的链表
    class Layer:
        def __init__(self, depth: int):
            self.prev = None
            self.next = None
            # depth表示使用次数
            self.depth = depth

            # 这个就是二级的hashmap 加上下面的二级链表 做成了LRU的缓存
            self.queue = {}
            # 二级链表头
            self.start = LFUCache.Node(-1)
            # 二级链表尾巴
            self.end = self.start

    def __init__(self, capacity: int):
        self.capacity = capacity

        # 这个就是一级的hashmap 加上下面的链表 做成了LFU的缓存
        self.data = {}
        # 这个map用于指向链表结点，如果重新设计的话，可以和上面的map合并的
        self.kToLayer = {}
        # 链表尾巴
        self.end_layer = None
        # 链表头
        self.top_layer = self.Layer(0)

    def get(self, key: int) -> int:
        r = self.data.get(key, -1)
        if r != -1:
            # 更新记录使用次数的链表
            self.kToLayer[key] = self.update_layer(self.kToLayer[key], key)
        return r

    def put(self, key: int, value: int) -> None:
        # 1. capacity为0的话直接不干了
        if self.capacity == 0:
            return
        # 2. 数据已经存在的话，就更新记录使用次数的链表
        if self.data.get(key) is not None:
            self.data[key] = value
            self.kToLayer[key] = self.update_layer(self.kToLayer[key], key)
            return

        # 3.1 如果超过了限度，就从链表头取出一个，删掉
        if len(self.data) >= self.capacity:
            key_to_del = self.pop_queue_from_layer(self.top_layer)
            self.data.pop(key_to_del)
            now = self.kToLayer[key_to_del]
            if len(now.queue) == 0 and now.depth > 0:
                self.clear_layer(now)
            self.kToLayer.pop(key_to_del)
        # 3.2 把新的加进去
        self.data[key] = value
        self.add_key_to_layer(self.top_layer, key)
        self.kToLayer[key] = self.top_layer

    # --------------下面都是链表操作的辅助方法，注意链表的穿插不要丢了节点---------------

    def add_key_to_layer(self, now: Layer, key: int):
        n = self.Node(key)
        now.queue[key] = n
        now.end.add(n)
        now.end = n

    def delete_key_of_layer(self, layer: Layer, key: int):
        node = layer.queue[key]
        if node == layer.end:
            layer.end = node.prev
        node.delete_self()
        layer.queue.pop(key)

    # 一级链表的更新（layer更新）
    def update_layer(self, now: Layer, key: int) -> Layer:
        self.delete_key_of_layer(now, key)

        # 注意那个depth+1 就是对应着频次的+1。ps 如果增加的值不定，就不应该用链表了，可能需要红黑树了
        # 1. 当前已是链表最后 即频次最高 ->需要创建新的layer
        if now.next is None:
            next_layer = self.Layer(now.depth + 1)
            self.add_key_to_layer(next_layer, key)
            self.insert_layer(now, next_layer)
            out = next_layer
        # 2. 下一个layer直接跨了好几个深度 ->需要创建新的layer
        elif now.next.depth > now.depth + 1:
            next_layer = self.Layer(now.depth + 1)
            self.add_key_to_layer(next_layer, key)
            self.insert_layer(now, next_layer)
            out = next_layer
        # 3. 下一个layer刚好是目标深度 ->不需要创建新的layer
        else:
            self.add_key_to_layer(now.next, key)
            out = now.next

        # 如果这一层空了，就把它删掉，节省空间
        if len(now.queue) == 0 and now.depth > 0:
            self.clear_layer(now)
        return out

    def insert_layer(self, now: Layer, target: Layer):
        if now.next is None:
            target.prev = now
            now.next = target
            self.end_layer = target
        else:
            target.prev = now
            target.next = now.next
            now.next.prev = target
            now.next = target

    def clear_layer(self, now: Layer):
        if now.next is None:
            now.prev.next = None
            self.end_layer = now.prev
        elif now.prev is None:
            now.next.prev = None
        else:
            now.prev.next = now.next
            now.next.prev = now.prev

    def pop_queue_from_layer(self, now: Layer) -> int:
        # 传进来时就是一级链表头了
        # for top layer
        if len(now.queue) == 0 and now.depth == 0:
            now = now.next

        # 取二级链表的第一个key
        key = now.start.next.key
        self.delete_key_of_layer(now, key)

        if len(now.queue) == 0 and now.depth > 0:
            self.clear_layer(now)
        return key
