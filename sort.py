import random


data_list, data_length = [], 128
for item in range(0, 128):
    data_list.append(round(random.random(), 2))


def half_search(data, search_value):
    # 二分查找法    前提条件是数组必须有序
    data_list.sort()
    data_length = len(data)
    start_index, end_index, mid_index = 0, data_length-1, data_length // 2

    while(mid_index):
        if data[mid_index] == search_value:
            return search_value, mid_index
        elif data[mid_index] < search_value:
            start_index = mid_index
            mid_index = (start_index + end_index) // 2
        elif data[mid_index] > search_value:
            end_index = mid_index
            mid_index = (start_index + end_index) // 2


#print(half_search(data=data_list, search_value=0.36))


#选择排序       #每次选择一个最小/大的元素
def choice_order(data):
    #从大到小排序
    news_order, temp_bigest_value = [], 0
    for i in range(128):
        if not data:
            return news_order
        temp_bigest_value, temp_index = data[0], 0
        for index, item in enumerate(data):
            if item > temp_bigest_value:
                temp_bigest_value, temp_index = item, index

        news_order.append(temp_bigest_value)
        del data[temp_index]

    return news_order


#print(choice_order(data_list))


#阶乘   递归的方式实现~   在内存上使用的是栈
def factorial(num):
    if num == 1:
        return num
    else:
        return factorial(num-1) * num


def factorial_cycle(num):       #函数内部内存使用的是堆结构
    sum = 1
    while(num):
        sum = sum * num
        num = num - 1

    return sum


#print(factorial_cycle(4))


#递归缩小规模
def run_itself(data):
    sum = 0
    if not data:
        return 0
    else:
        return sum+data[0] + run_itself(data[1:])


#print(run_itself(data_list))


#快速排序   分而治之
def quick_sort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i <= pivot]
        more = [i for i in data[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(more)


#print(quick_sort(data_list))

#合并排序 小 < 大
def merge_sort(data):

    if len(data) < 2:
        return data

    def merge_list(list_a, list_b):
        #两个有序数组合并
        data, i, j = [], 0, 0
        while(True):
            if len(list_b) <= j:
                data.extend(list_a[i:])
                break
            if len(list_a) <= i:
                data.extend(list_b[j:])
                break

            if list_a[i] < list_b[j]:
                data.append(list_a[i])
                i = i + 1
            else:
                data.append(list_b[j])
                j = j + 1

        return data

    def part_to(data):
        #数组分离
        if len(data) <= 1:
            return data

        if len(data) == 2:
            if data[0] > data[1]:
                return [data[1], data[0]]
            else:
                return [data[0], data[1]]

        mid = len(data) // 2
        left = part_to(data[:mid])
        right = part_to(data[mid:])

        result = merge_list(left, right)
        return result

    return part_to(data=data)


# print(merge_sort(data=data_list))


from collections import deque


def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L


def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = L_length // 2
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]


def main():
    L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))


if __name__ == '__main__':
    main()
