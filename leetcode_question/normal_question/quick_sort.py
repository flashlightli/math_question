def quick_sort(nums):
    # 递归快排
    if len(nums) <= 1:
        return nums

    midpivot = nums[0]
    left = [item for item in nums[1:] if item <= midpivot]
    right = [item for item in nums[1:] if item > midpivot]

    return quick_sort(left) + [midpivot] + quick_sort(right)


print(quick_sort([3, 1, 6, 2, 4]))


def quick_sort_2(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr

    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)

    return arr


def partition(arr, start, end):
    # 分区操作，返回基准线下标
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # 此时start = end
    arr[start] = pivot
    print("单次", arr)
    return start


print(quick_sort_2([3, 1, 6, 2, 4]))


def quick_sort(demo):
    if len(demo) <= 1:
        return demo

    stack = []
    stack.append(len(demo) - 1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition_2(demo, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)

    return demo


def partition_2(demo, l, r):
    pivot = demo[l]
    while l < r:
        while l < r and pivot <= demo[r]:
            r -= 1
        demo[l] = demo[r]
        while l < r and pivot >= demo[l]:
            l += 1
        demo[r] = demo[l]

    demo[l] = pivot
    return l


class SkipListNode(object):
    def __init__(self):
        self.val = None
        self.next = None
        self.down = None


def skip_list_search(head, target):
    """
    跳表查询的实现  插入的话节点是随机的
    """
    tmp = head
    curr = head
    while curr:
        if curr.val == target:
            return True
        else:
            tmp = curr if curr.down else tmp
            curr = curr.next

    return skip_list_search(tmp, target)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    """
    再简单总结下堆排序的基本思路：
　　a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
　　b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
　　c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    print(arr)
    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)
        print(i, arr)

    return arr


print(heapSort([2, 7, 4, 3, 8, 9]))