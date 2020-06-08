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

