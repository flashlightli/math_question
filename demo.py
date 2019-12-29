#53             二分查找法
show_number = 0

def erfen(a, lis_b):
    len_b = len(lis_b)
    if not lis_b:
        return 0
    if len_b == 1 and lis_b[0] == a:
        return 1
    if len_b == 1 and lis_b[0] != a:
        return 0
    temp = len_b // 2
    if lis_b[temp] > a:
        return erfen(a, lis_b[:temp])
    elif lis_b[temp] < a:
        return erfen(a, lis_b[temp:])
    else:
        return erfen(a, lis_b[temp:]) + erfen(a, lis_b[:temp])


def erfen_find(list_b, start_num, end_num):
    temp = (start_num + end_num) // 2
    if not list_b:
        return
    if end_num - start_num == 1:
        if list_b[start_num] == start_num:
            return end_num
        else:
            return start_num

    if list_b[temp] != temp:
        return erfen_find(list_b, start_num=start_num, end_num=temp)
    else:
        return erfen_find(list_b, start_num=temp, end_num=end_num)
#54                 二叉树


class TreeNode(object):
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
#
#
# leaf_6 = TreeNode(value=99)
# leaf_1 = TreeNode(value=2)
# leaf_2 = TreeNode(value=4, left_node=leaf_6)
# leaf_3 = TreeNode(value=6)
# leaf_4 = TreeNode(value=8)
# other_1 = TreeNode(value=3, left_node=leaf_1, right_node=leaf_2)
# other_2 = TreeNode(value=7, left_node=leaf_3, right_node=leaf_4)
# root_1 = TreeNode(value=5, left_node=other_1, right_node=other_2)
# list_value = []


def front_order(root_1):            #前序
    if not root_1:
        return
    print(root_1.value)
    front_order(root_1.left_node)
    front_order(root_1.right_node)


def middle_order(root_1):           #中序
    if not root_1:
        return

    middle_order(root_1.left_node)
    print(root_1.value)
    middle_order(root_1.right_node)


def post_order(root_1):             #后序
    if not root_1:
        return

    post_order(root_1.left_node)
    post_order(root_1.right_node)
    print(root_1.value)

#55                 二叉树


def get_deepth(root_1):             #获取深度
    if not root_1:
        return 0

    length_temp = max(get_deepth(root_1.left_node), get_deepth(root_1.right_node))
    return 1 + length_temp


#57
#和为S的数字         指针从两端到中间

def get_sum_number(number_list, target_number):
    i, end_index = 0, len(number_list) - 1
    if len(number_list) < 2:
        return

    while(number_list[i] < number_list[end_index]):     #两个指针，一个从头部向后走，一个从尾部向前走
        if number_list[i] + number_list[end_index] > target_number:
            end_index -= 1
        elif number_list[i] + number_list[end_index] < target_number:
            i += 1
        else:
            print(number_list[i], number_list[end_index])
            break


#56          位运算（异或）     数组中只出现一次的数字
def get_number_count(number_list):
    temp = 0
    for i in number_list:
        temp ^= i

    index = 0
    while temp & 1 == 0:        #位数向前移， 找到位数是1的值
        temp >>= 1
        index += 1

    a, b = 0, 0
    for i in number_list:
        i = i >> index             #位数向后移动index位
        if i & 1 == 0:             #分成两个部分，一部分的数在位置index为0，另一部分在位置index为1
            a ^= i
        else:
            b ^= i
    return [a, b]


#++++++给定一个数组，其中只有一个数x出现一次，别的数都出现3次，找出这个数x
# 可以设置一个长度为32的int数组。统计每位上出现1的次数，如果次数能被3整除，说明x该位上为0，否则为1
def three_in_once(number_list):
    byte_list = [0] * 32
    for i in number_list:
        for by in range(0, 32):
            byte_list[by] += ((i >> by) & 1)

    number = 0
    for index, item in enumerate(byte_list):
        if not isinstance(item/3, int):
            number += (item%3) * (2**index)

    return number

#59         栈的应用
def get_number_big(number_list, number_len):
    temp_stack, temp_index = [], []
    for i in range(0, len(number_list)):
        if not temp_stack:                      #判断是否为空
            temp_stack.append(number_list[i])
            temp_index.append(i)
            continue

        if temp_stack[0] <= number_list[i]:         #判断新插入的元素是否大于之前的元素
            temp_stack = [number_list[i]]
            temp_index = [i]
        else:
            for index, item in enumerate(temp_stack):
                if i - temp_index[index] >= number_len:     #检测最大元素列表 元素是否超过滑窗
                    temp_stack.pop(index)
                    temp_index.pop(index)

                if item > number_list[i]:           #不大于就插入到最大元素列表里
                    temp_stack.append(number_list[i])
                    temp_index.append(i)
                else:                               #对最大元素列表大小排序
                    temp_stack = [temp_stack[0], number_list[i]]
                    temp_index = [temp_index[0], i]
                    break

        if number_len-1 <= i:
            print(temp_stack[0])


#数组中的逆序对  合并排序过程中进行统计
def get_desc_order(number_list):
    pass


#求股票的最大利润   动态规划  63
def get_biggest_money(number_list):
    if not number_list:
        return 0
    cur_diff = 0
    maxn = 0
    #求前n-1个数字的最大差值， 后一个数减去前一个数的差值加上前面的最大差值就是当前的差值
    for i in range(1, len(number_list)):
        if number_list[i] - number_list[i-1] + cur_diff > 0:
            #如果这个差值大于0
            cur_diff = number_list[i] - number_list[i-1] + cur_diff
        else:
            cur_diff = 0

        maxn = max(maxn, cur_diff)

    return maxn


#最大子序和        动态规划
def biggest_child_sum(number_list):
    if not number_list:
        return

    sum_list = number_list[0]
    curr_sum = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] + curr_sum > number_list[i]:
            #前面n-1个的和+当前的值 >当前的值， 说明是增加的
            curr_sum = number_list[i] + curr_sum
        else:
            curr_sum = number_list[i]

        sum_list = max(curr_sum, sum_list)
    return sum_list


#乘积最大子序列            #动态规划
def product_child(number_list):
    if not number_list:
        return

    #根据观察，我们不仅需要记录下第 i - 1 个状态下的连续子数组的最大乘积last_max( 大多数情况下为正 )，
    # 还需要记录下第 i - 1个状态下的连续子数组的最小乘积last_min，从而得出第 i 个状态的连续子序列的最大乘积为
    #  cur_max = max( max( last_max * array[ i ], last_min * array[ i ] ) , array[ i ] ); 
    result = number_list[0]
    curr_max, curr_min = number_list[0], number_list[0]
    #需要多存储一个最小的值
    for i in range(1, len(number_list)):
        #记录当前的最大乘积值和最小乘积值  顺序不能变
        curr_max = max(number_list[i], max(number_list[i] * curr_min, number_list[i] * curr_max))
        curr_min = min(number_list[i], min(number_list[i] * curr_min, number_list[i] * curr_max))
        result = max(curr_max, result)

    return result


#给定不同面额的硬币 coins 和一个总金额 amount。  返回硬币数  动态规划
def give_coin(coin_list, money):
    if not money:
        return 0

    if not coin_list:
        return -1

    Min = [x for x in range(money+1)]       #一个数组暂存配置每一个money的硬币数量
    for i in range(1, money+1):
        for j in range(len(coin_list)):
            #硬币额度小于需要配置的钱币数 且 当前金额-硬币金额 的硬币数< 当前硬币数
            if coin_list[j] <= i and Min[i - coin_list[j]] + 1 < Min[i]:
                Min[i] = Min[i - coin_list[j]] + 1

    print(Min[1::1])
# give_coin([186, 419, 83, 408], 6249)
# give_coin([1, 3, 5], 11)


#leetcode 101 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？ 3个节点是5种   https://www.youtube.com/watch?v=HWJEMKWzy-Q
def get_tree_number(node_number):
    node_list = [1] + [1] * node_number
    for i in range(2, node_number+1):
        temp_sum = 0
        for j in range(0, i):
            temp_sum += node_list[j] * node_list[i-j-1]
        node_list[i] = temp_sum

    print(node_list[-1])
#get_tree_number(4)

#问题同上 输出这些二叉树
def print_tree_detail(node_number):
    node_list = [[None], [1]] + [None] * (node_number - 1)
    for i in range(2, node_number + 1):
        temp_list = []
        for j in range(0, i):
            pass
        #未解出来


#从起始点到目标点的路径数。如：从（0.，0）出发到（2，3）点的路径数目
def get_path_num(x=0, y=0, target_x=0, target_y=0):

    if x > target_x or y > target_y:
        return 0

    if x == target_x and y == target_y:
        return 1

    return get_path_num(x=x+1, y=y, target_x=target_x, target_y=target_y) + get_path_num(x=x, y=y+1, target_x=target_x, target_y=target_y)


#爬楼梯            斐波那契数列
def up_stairs(number):
    num_list = [1, 1, 2] + [None] * number
    for i in range(3, number+1):
        num_list[i] = num_list[i-1] + num_list[i-2]

    print(num_list[i])

#up_stairs(4)


#LeetCode236 二叉树最近公共节点  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#递归解法（分治）
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right
#
#
# node_7 = TreeNode(x=7)
# node_4 = TreeNode(x=4)
# node_8 = TreeNode(x=8)
# node_0 = TreeNode(x=0)
# node_2 = TreeNode(x=2, left=node_4, right=node_7)
# node_6 = TreeNode(x=6)
# node_1 = TreeNode(x=1, left=node_0, right=node_8)
# node_5 = TreeNode(x=5, left=node_6, right=node_2)
# root_node = TreeNode(x=3, left=node_5, right=node_1)

def get_father(root_node, node_tar_1, node_tar_2):
    #如果一个节点是目标值，就返回该值，如果一个节点的左右子树返回的值符合条件，即最近公共节点就是该子树

    if root_node.val == node_tar_1:
        return node_1

    if root_node.val == node_tar_2:
        return node_2

    if not root_node.left:
        return None

    if not root_node.right:
        return None

    left_val = get_father(root_node.left, node_tar_1, node_tar_2)
    right_val = get_father(root_node.right, node_tar_1, node_tar_2)
    if not left_val:
        return right_val

    if not right_val:
        return left_val

    return root_node.val


# print(get_father(root_node=root_node, node_tar_1=6, node_tar_2=4))


#3的幂  对数运算
def is_three(number):
    import math
    temp = math.log(number, 3)  #math.log(9, 3)=2


#最长上升子序列 leetcode 300   [10,9,2,5,3,7,101,18]
def longest_list(number_list):
    number_rise = []

    def erfen_demo(number_rise, num):
        """后续可以改成二分更改"""
        if num > number_rise[-1]:
            number_rise.append(num)
            return number_rise

        for index, item in enumerate(number_rise):
            if num <= item:
                number_rise[index] = num
                return number_rise

    for number in number_list:
        if not number_rise:
            number_rise.append(number)
            continue

        number_rise = erfen_demo(number_rise, number)

    return len(number_rise)


#LeetCode 130 二维数组，被围绕的区域  找到被包围的区域，其实也可以找没有被包围的区域，除了这些区域都是1
def change_around_area(board):
    row_len = len(board)
    replace_item = []


#leetcode371  两个整数之和        ^异或
def sum_number(number_1, number_2):
    if number_1 == -number_2:
        return 0

    while(number_2):
        all_have = (number_1 & number_2) << 1
        number_1 = number_1 ^ number_2
        number_2 = all_have

    return number_1


# print(sum_number(2, -2))

#二分插入function nums是有序的（默认从小到大）
def erfen_insert(nums, target):

    if not nums:
        return [target]

    if len(nums) == 1:
        return nums + [target] if target > nums[0] else [target] + nums

    mid = len(nums) // 2
    if nums[mid] < target:
        return nums[:mid] + erfen_insert(nums[mid:], target=target)
    else:
        return erfen_insert(nums[:mid], target=target) + nums[mid:]


#leetcode 315   计算右侧小于当前元素的个数  需要优化 总体nlgn（二分查找插入）  还需优化
def countSmaller(nums):
    result = []
    order_list = []
    news_nums = list(reversed(nums))
    for i in range(0, len(news_nums)):
        order_list = erfen_insert(order_list, target=news_nums[i])
        result.append(order_list.index(news_nums[i]))

    return list(reversed(result))


#print(countSmaller(nums=[5,2,6,1]))


#LeetCode 172 阶乘后的零     计算5的个数  因为2的个数远远大于5的个数
def trailingZeroes(num):
    res = 0

    while num >= 5:
        res += num // 5
        num //= 5
    return res

#print(trailingZeroes(26))

#二叉树左子树之和
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right
#
# node_7 = TreeNode(x=7)
# node_4 = TreeNode(x=4)
# node_8 = TreeNode(x=8)
# node_0 = TreeNode(x=0)
# node_2 = TreeNode(x=2, left=node_4, right=node_7)
# node_6 = TreeNode(x=6)
# node_1 = TreeNode(x=1, left=node_0, right=node_8)
# node_5 = TreeNode(x=5, left=node_6, right=node_2)
# root_node = TreeNode(x=3, left=node_5, right=node_1)

def sum_tree(root_node, is_left=False):
    if not root_node or not root_node.val:
        return 0

    value = root_node.val if is_left else 0

    return value + sum_tree(root_node=root_node.left, is_left=True) + sum_tree(root_node=root_node.right, is_left=False)

#node_5 + node_6 + node_4
#print(sum_tree(root_node=root_node))



#链表翻转
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def revert_list(head):
    if not head:
        return None

    p = head
    cur, pre = None, None
    while p is not None:
        cur = p.next        #循环节点下一节点暂存
        p.next = pre        #上一节点为循环节点的下一节点
        pre = p             #循环节点成为了上一节点
        p = cur             #更新循环节点
    return pre

demo_4 = ListNode(val=5)
demo_3 = ListNode(val=4,next=demo_4)
demo_2 = ListNode(val=3,next=demo_3)
demo_1 = ListNode(val=2,next=demo_2)


# first = revert_list(demo_1)
# while first:
#     print(first.val)
#     first = first.next


#leetcode 16  双指针 数组
class Solution_16:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        near_value = 0
        if len(nums) < 3:
            return

        near_value = nums[0] + nums[1] + nums[2]
        for index, value in enumerate(nums):
            i = index + 1
            j = len(nums) - 1
            while(i<j):
                temp_value = nums[i] + nums[j] + value
                if temp_value < target:
                    near_value = temp_value if abs(target - near_value) > abs(target - temp_value) else near_value
                    i = i + 1
                else:
                    near_value = temp_value if abs(target - near_value) > abs(target - temp_value) else near_value
                    j = j - 1

        return near_value

# demo = Solution_16()
# print(demo.threeSumClosest(nums=[-3,-2,-5,3,-4], target=-1))


#leetcode 11     双指针 盛水最多的容器 [1,8,6,2,5,4,8,3,7] 49
class Solution_11:
    def maxArea(self, height):
        """如果左边的值大于右边的，就从右边的向左来，如果左边的值小于右边的，就从左边的向右来，"""
        max_value = 0

        i, j = 0, len(height) - 1
        while(i < j):
            max_value = max(min(height[i], height[j])*(j-i), max_value)
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1

        return max_value


# demo = Solution_11()
# print(demo.maxArea(height=[1,2,5,3]))


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

node_7 = TreeNode(x=5)
node_8 = TreeNode(x=5)
node_0 = TreeNode(x=20)
node_4 = TreeNode(x=15, left=node_8, right=node_0)
node_2 = TreeNode(x=2, left=node_4, right=node_7)
node_6 = TreeNode(x=6)
node_1 = TreeNode(x=1, left=node_0, right=node_8)
node_5 = TreeNode(x=5, left=node_6, right=node_2)
root_node = TreeNode(x=10, left=node_7, right=node_4)

#leetcode 98 验证二叉搜索树 符合条件
class Solution_98:
    def isValidBST(self, root):
        if not root:
            return True
        return self.range_root(root, left_val=None, right_val=None)

    def range_root(self, root, left_val, right_val):
        l_val, r_val = True, True

        if not root:
            return False

        if root.left and root.val > root.left.val:
            if left_val and root.left.val > left_val:
                l_val = self.range_root(root.left, left_val=left_val, right_val=root.val)
            elif left_val and root.left.val <= left_val:
                return False
            else:
                l_val = self.range_root(root.left, left_val=left_val, right_val=root.val)
        elif root.left:
            return False

        if not l_val:
            return False

        if root.right and root.val < root.right.val:
            if right_val and root.right.val < right_val:
                r_val = self.range_root(root.right, left_val=root.val, right_val=right_val)
            elif right_val and root.right.val >= right_val:
                return False
            else:
                r_val = self.range_root(root.right, left_val=root.val, right_val=right_val)
        elif root.right:
            return False

        return l_val and r_val

# demo = Solution_98()
# print(demo.isValidBST(root_node))


#leetcode 101   判断二叉树是否对称  层序遍历 检查每层的回文数组
class Solution_101:

    def isSymmetric(self, root):
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)


# demo = Solution_101()
# print(demo.isSymmetric(root_node))


#leetcode 105   从前序与中序遍历序列构造二叉树

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_105:
    root = None

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return

        temp_root_value = preorder[0]
        self.root = TreeNode(x=temp_root_value)
        root_in_location = inorder.index(temp_root_value)
        print(root_in_location)
        print(preorder[1:root_in_location+1], inorder[:root_in_location])
        print(preorder[root_in_location+1:], inorder[root_in_location+1:])

        self.buildLeftTreeNode(preorder=preorder[1:root_in_location+1], inorder=inorder[:root_in_location], root=self.root)
        self.buildRightTreeNode(preorder=preorder[root_in_location+1:], inorder=inorder[root_in_location+1:],
                                root=self.root)
        return self.root

    def buildLeftTreeNode(self, preorder, inorder, root):
        if not preorder or not inorder:
            return

        if not self.root:
            return

        temp_root_value = preorder[0]
        print(preorder, inorder, temp_root_value)
        root.left = TreeNode(x=temp_root_value)
        root_in_location = inorder.index(temp_root_value)
        self.buildLeftTreeNode(preorder=preorder[1:root_in_location+1], inorder=inorder[:root_in_location],
                               root=root.left)
        self.buildRightTreeNode(preorder=preorder[root_in_location + 1:], inorder=inorder[root_in_location + 1:],
                                root=root.left)
        return

    def buildRightTreeNode(self, preorder, inorder, root):
        if not preorder or not inorder:
            return

        if not self.root:
            return

        temp_root_value = preorder[0]
        print(preorder, inorder, temp_root_value)
        root.right = TreeNode(x=temp_root_value)
        root_in_location = inorder.index(temp_root_value)
        self.buildLeftTreeNode(preorder=preorder[1:root_in_location+1], inorder=inorder[:root_in_location],
                               root=root.right)
        self.buildRightTreeNode(preorder=preorder[root_in_location + 1:], inorder=inorder[root_in_location + 1:],
                                root=root.right)
        return


# demo = Solution_105()
# demo.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])

#leetcode106        从前序与中序遍历序列构造二叉树
class Solution_106:
    root = None

    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return

        temp_root_value = postorder[-1]
        self.root = TreeNode(x=temp_root_value)
        root_in_location = inorder.index(temp_root_value)
        print(root_in_location)
        print(postorder[:root_in_location], inorder[:root_in_location])
        print(postorder[root_in_location:-1], inorder[root_in_location + 1:])
        self.buildLeftTreeNode(inorder=inorder[:root_in_location], postorder=postorder[:root_in_location],
                               root=self.root)
        self.buildRightTreeNode(inorder=inorder[root_in_location + 1:], postorder=postorder[root_in_location:-1],
                                root=self.root)
        return self.root

    def buildLeftTreeNode(self, inorder, postorder, root):
        if not postorder or not inorder:
            return

        if not self.root:
            return

        temp_root_value = postorder[-1]
        print(postorder, inorder, temp_root_value)
        root.left = TreeNode(x=temp_root_value)
        root_in_location = inorder.index(temp_root_value)
        self.buildLeftTreeNode(inorder=inorder[:root_in_location], postorder=postorder[:root_in_location],
                               root=root.left)
        self.buildRightTreeNode(inorder=inorder[root_in_location + 1:], postorder=postorder[root_in_location:-1],
                                root=root.left)
        return

    def buildRightTreeNode(self, inorder, postorder, root):
        if not postorder or not inorder:
            return

        if not self.root:
            return

        temp_root_value = postorder[-1]
        print(postorder, inorder, temp_root_value)
        root.right = TreeNode(x=temp_root_value)
        root_in_location = inorder.index(temp_root_value)
        self.buildLeftTreeNode(inorder=inorder[:root_in_location], postorder=postorder[:root_in_location],
                               root=root.right)
        self.buildRightTreeNode(inorder=inorder[root_in_location + 1:], postorder=postorder[root_in_location:-1],
                                root=root.right)
        return


# demo = Solution_106()
# demo.buildTree(inorder=[9,3,15,20,7], postorder=[9,15,7,20,3])


#leetcode129       求根到叶子节点之和
class Solution_129:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.sum_tree_val(root=root, pre_value=root.val)

    def sum_tree_val(self, root, pre_value):
        if not root.left and not root.right:
            return pre_value

        if not root.left:
            return self.sum_tree_val(root.right, pre_value=pre_value*10+root.right.value)

        if not root.right:
            return self.sum_tree_val(root.left, pre_value=pre_value * 10 + root.left.value)

        return self.sum_tree_val(root.left, pre_value=pre_value*10+root.left.value) + self.sum_tree_val(root.right, pre_value=pre_value * 10 + root.right.value)


#leetcode 102           二叉树的层序遍历
class Solution_102:
    temp_stack = []
    result = []
    layer = 1

    def levelOrder_init(self, root):
        #二叉树的层序遍历
        if not root:
            return []

        self.temp_stack = [root]
        while(self.temp_stack):
            node = self.temp_stack.pop(0)
            if not node:
                continue
            self.result.append(node.val)
            self.temp_stack.append(node.left)
            self.temp_stack.append(node.right)

        return self.result

    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        self.temp_stack = [(root, 1)]
        while(self.temp_stack):
            node, layer = self.temp_stack.pop(0)
            if not node:
                continue
            if self.layer != layer:
                self.layer += 1
                self.result.append([node.val])
                self.temp_stack.append((node.left, layer+1))
                self.temp_stack.append((node.right, layer+1))
            else:
                last_result = self.result.pop()
                last_result.append(node.val)
                self.result.append(last_result)
                self.temp_stack.append((node.left, layer+1))
                self.temp_stack.append((node.right, layer+1))

        return self.result

#
# demo = Solution_102()
# print(demo.levelOrder_init(root=root_node))


#leetcode103    二叉树的锯齿形层次遍历         广度优先 依赖队列
class Solution_103:

    def zigzagLevelOrder(self, root):
        if not root: return []
        cur, nex, tmp, res = [root], [], [], []
        direction = "left"
        while cur:
            for r in cur:
                tmp.append(r.val)
                if r.left: nex.append(r.left)
                if r.right: nex.append(r.right)
            if direction == "left":
                res.append(tmp[:])
                direction = "right"
            else:
                reverst_tmp = []
                for i in tmp:
                    reverst_tmp.insert(0, i)
                res.append(reverst_tmp)
                direction = "left"
            cur, nex, tmp = nex, [], []
        return res


#leetcode 3 无重复字符的最长子串 长度       求出正确的滑动窗口  可用指针法    无重复--字典or set类型
class Solution_3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_str = list(s)
        max_len = 0
        temp_list = []
        temp_dic = {}

        for index, value in enumerate(list_str):
            if value in temp_list:
                max_len = max(max_len, len(temp_list))
                diff_index = index - temp_dic.get(value)
                temp_list = temp_list + [value]
                temp_list = temp_list[-diff_index:]
            else:
                temp_list.append(value)
                max_len = max(max_len, len(temp_list))
            temp_dic[value] = index

        return max_len


#LeetCode 136   只出现一次的数字        位运算
class Solution_136:
    def singleNumber(self, nums) -> int:
        sum_nums = 0
        for i in nums:
            sum_nums = sum_nums ^ i

        return sum_nums


#leetcode 05 最长回文子串(正序和倒序一样的字符串)   使用的是双指针法 测试用例： #babad  abbe  aaa cccc
class Solution_5:
    def longestPalindrome(self, s: str) -> str:
        str_list = list(s)
        max_str_list = str_list[0] if len(str_list) else []
        for index in range(1, len(str_list)-1):
            i, j = index - 1, index + 1
            temp_list = [str_list[index]]
            while(i >= 0 and j < len(str_list)):
                if str_list[i] == str_list[j]:
                    temp_list.insert(0, str_list[i])
                    temp_list.append(str_list[j])
                    max_str_list = temp_list if len(temp_list) > len(max_str_list) else max_str_list
                    i = i - 1
                    j = j + 1
                else:
                    max_str_list = temp_list if len(temp_list) > len(max_str_list) else max_str_list
                    break

        for index in range(0, len(str_list) - 1):
            if str_list[index] == str_list[index+1]:
                i, j = index - 1, index + 2
                temp_list = [str_list[index], str_list[index+1]]
                max_str_list = temp_list if len(temp_list) > len(max_str_list) else max_str_list
            else:
                continue

            while (i >= 0 and j < len(str_list)):
                if str_list[i] == str_list[j]:
                    temp_list.insert(0, str_list[i])
                    temp_list.append(str_list[j])
                    max_str_list = temp_list if len(temp_list) > len(max_str_list) else max_str_list
                    i = i - 1
                    j = j + 1
                else:
                    max_str_list = temp_list if len(temp_list) > len(max_str_list) else max_str_list
                    break
        return "".join(max_str_list)


#leetcode523    连续的子数组和
class Solution_523:
    def checkSubarraySum(self, nums, k):
        if len(nums) <= 1:
            return False

        tmp_save = [nums[0]+nums[1]]
        if nums[0]+nums[1] == 0:
            return True

        if k and (nums[0]+nums[1]) % k == 0:
            return True

        index = 2
        while(index < len(nums)):
            temp = []
            if not k:
                if nums[index-1] + nums[index] == 0:
                    index += 1
                    return True
                else:
                    index += 1
                    continue
            for item in tmp_save:
                if (item + nums[index]) % k == 0:
                    return True
                else:
                    temp.append(item + nums[index])
            if (nums[index-1] + nums[index]) % k == 0:
                return True
            else:
                temp.append(nums[index-1] + nums[index])

            tmp_save = temp
            index += 1
        return False


#leetcode 718 最长重复子数组   动态规划（画表格解决）     时间空间复杂度极低的方法=滑动窗口解法
#https://blog.csdn.net/m0_37477175/article/details/80273231
class Solution_718:
    def findLength(self, A, B) -> int:
        l1 = len(A)
        l2 = len(B)

        dp_list = [[0 for j in range(l2+1)] for i in range(l1+1)]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if A[i-1] == B[j-1]:
                    dp_list[i][j] = dp_list[i-1][j-1] + 1

        return max(max(item) for item in dp_list)


# demo = Solution_718()
# print(demo.findLength2(B=[1,0,0,0,1], A=[1,0,0,1,1]))
#leetcode 583 两个字符串的删除操作 == 求最长公共子序列问题
class Solution_583:
    def minDistance(self, word1: str, word2: str) -> int:
        A, B = list(word1), list(word2)
        l1 = len(A)
        l2 = len(B)

        dp_list = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if A[i - 1] == B[j - 1]:
                    dp_list[i][j] = dp_list[i-1][j-1] + 1
                else:
                    dp_list[i][j] = max(dp_list[i-1][j], dp_list[i][j-1])

        max_len = max(max(item) for item in dp_list)
        return l1 + l2 - 2 * max_len


# demo = Solution_583()
# print(demo.minDistance(word1="food", word2="money"))


#LeetCode 61        旋转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_61:      #先连成环
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head


#波动数组   求生成波动数组所需走的最少步数，每步操作把元素值+1 or -1
class WaveList(object):
    def get_wave_short_step(self, list_demo):
        avg_num = round(sum(list_demo) / len(list_demo))
        for item in list_demo:
            pass


#leetcode 75  三指针      0 , 1, 2三个元素O(n) 常熟空间复杂度排序
class Solution_75(object):
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums

        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[1], nums[0] = nums[0], nums[1]

        pre, curr, end = 0, 0, len(nums) - 1

        while(curr <= end):
            if nums[curr] == 0:
                nums[pre], nums[curr] = nums[curr], nums[pre]
                pre += 1
                curr += 1
            elif nums[curr] == 2:
                nums[end], nums[curr] = nums[curr], nums[end]
                end -= 1
            else:
                curr += 1


# demo = Solution_75()
# print(demo.sortColors(nums=[2,1,0]))

#leetcode 33 搜索旋转排序数组
class Solution_33:
    def search(self, nums, target):
        mid = len(nums) // 2
        p1, p2 = 0, len(nums) - 1
        position = -1
        if not nums or target not in nums:
            return -1

        while(mid >= p1 and mid <= p2):
            if nums[mid] == target:
                position = mid
                break
            if nums[p1] == target:
                position = p1
                break
            if nums[p2] == target:
                position = p2
                break

            if nums[mid] > nums[p1] and nums[mid] > nums[p2]:
                if nums[mid] > target > nums[p1]:
                    mid, p2 = (p1 + mid) // 2, mid
                    continue
                else:
                    mid, p1 = (p2 + mid) // 2, mid
                    continue
            if nums[mid] < nums[p1] and nums[mid] < nums[p2]:
                if nums[p2] > target > nums[mid]:
                    mid, p1 = (p2 + mid) // 2, mid
                    continue
                else:
                    mid, p2 = (p1 + mid) // 2, mid
                    continue
            if nums[p1] < target < nums[p2]:
                if target > nums[mid]:
                    mid, p1 = (mid + p2) // 2, mid
                else:
                    mid, p2 = (mid + p1) // 2, mid

        return position


# demo = Solution_33()
# print(demo.search(nums=[4,5,6,7,0,1,2], target=6))


#LeetCode 42接雨水     双指针
class Solution_42:
    def trap(self, height):
        rain = 0
        if not height or len(height) <= 2:
            return rain

        i, j = 0, len(height) - 1
        max_high = 0
        while(i < j):
            if height[i] < height[j]:
                max_high = max(max_high, min(height[i], height[j]))
                rain += (max_high - height[i]) if max_high > height[i] else 0
                i += 1
            else:
                max_high = max(max_high, min(height[i], height[j]))
                rain += (max_high - height[j]) if max_high > height[j] else 0
                j -= 1

        return rain


# demo = Solution_42()
# print(demo.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))


#leetcode 63 计算不同路径     动态规划
class Solution_63:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0

        temp_list = []
        for i in range(len(obstacleGrid)):
            temp_list.append([])
            for j in range(len(obstacleGrid[0])):
                temp_list[i].append(0)

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    temp_list[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    temp_list[i][j] = 1
                if i == 0 and j > 0:
                    temp_list[i][j] = temp_list[i][j - 1]
                if i > 0 and j == 0:
                    temp_list[i][j] = temp_list[i-1][j]
                if i > 0 and j > 0:
                    temp_list[i][j] = temp_list[i-1][j] + temp_list[i][j-1]

        return temp_list[-1][-1]

# demo = Solution_63()
# print(demo.uniquePathsWithObstacles([
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]))


#leetcode 54  螺旋矩阵输出    数组
class Solution_54:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        temp_list = [] + matrix[0]
        for i in range(1, len(matrix)-1):
            if not matrix[i]:
                continue
            temp_list.append(matrix[i].pop(-1))

        if len(matrix) != 1:
            third_list = []
            for i in matrix[-1]:
                third_list.insert(0, i)
            temp_list += third_list

        for i in range(len(matrix)-2, 1, -1):
            if not matrix[i]:
                continue
            temp_list.append(matrix[i].pop(0))

        return temp_list + self.spiralOrder(matrix[1:-1])


# demo = Solution_54()
# print(demo.spiralOrder(
# [[1,2,3,4],
#  [5,6,7,8],
#  [9,10,11,12],
#  [13,14,15,16]
#  ]
# ))


#leetcode 34  在排序数组中查找元素的第一个和最后一个位置
class Solution_34:
    def searchRange(self, nums, target):
        start, mid, end = 0, len(nums) // 2, len(nums) - 1
        start_index, end_index = 0, 0
        result = [-1, -1]
        if target not in nums:
            return result

        while(True):
            if nums[mid] < target:
                start, mid = mid, int(0.5+(mid + end)/2)
                continue
            if nums[mid] > target:
                end, mid = mid, (mid + start) // 2
                continue
            if nums[mid] == target:
                result[0], result[1] = mid, mid
                start_index, end_index = mid, mid
                break

        while(nums[start_index]==target):
            result[0] = start_index
            if start_index == 0:
                break
            if start_index > 0:
                start_index -= 1

        while (nums[end_index] == target):
            result[1] = end_index
            if end_index == len(nums) - 1:
                break
            if end_index < len(nums) - 1:
                end_index += 1
        return result


# demo = Solution_34()
# print(demo.searchRange(nums = [1,2,3], target = 3))


#leetcode 56合并区间    [[1,3],[2,6]]  ==> [[1,6]]
class Solution_56:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x: x[0])
        new_list = [intervals[0]]
        for index, num_list in enumerate(intervals):
            if not index:
                continue

            last_num_list = new_list.pop()
            if last_num_list[1] >= num_list[0]:
                new_list.append([min(num_list[0], last_num_list[0]), max(num_list[1], last_num_list[1])])
            else:
                new_list.append(last_num_list)
                new_list.append(num_list)

        return new_list


#leetcode 72 编辑距离  动态规划 word1-->word2所需步骤最少的操作(插入、删除、替换)数目 word1 = "horse", word2 = "ros"  输出: 3
#画方格图 左--->右 + 1   上------>下  + 1    左上 ----->右下 判断是否相等再+1
class Solution_72:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = list(word1)
        word2 = list(word2)
        if not word2:
            return len(word1)
        if not word1:
            return len(word2)

        stash_list = [[0 for item in range(0, len(word2)+1)] for item in range(0, len(word1)+1)]
        for index, value in enumerate(stash_list[0]):
            stash_list[0][index] = index

        for index, value in enumerate(stash_list):
            stash_list[index][0] = index

        for index_1, item_1 in enumerate(word1):
            for index_2, item_2 in enumerate(word2):
                if item_2 == item_1:
                    min_value = min(stash_list[index_1 + 1][index_2]+1, stash_list[index_1][index_2 + 1]+1,
                                 stash_list[index_1][index_2])
                    stash_list[index_1+1][index_2+1] = min_value
                else:
                    min_value = min(stash_list[index_1 + 1][index_2]+1, stash_list[index_1][index_2 + 1]+1,
                                 stash_list[index_1][index_2]+1)
                    stash_list[index_1+1][index_2+1] = min_value

        return stash_list[-1][-1]


# demo = Solution_72()        #测试用例 #kitten  sitting          oogoe   oge
# print(demo.minDistance(word2="oogoe", word1="oge"))


#LeetCode 309   最佳买卖股票时机含冷冻期 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#测试用例  # [6,1,3,2,4,7]   [1,2,3,0,2]
class Solution_309:
    def maxProfit(self, prices) -> int:
        if not prices or len(prices) == 1:
            return 0

        second_income = prices[1] - prices[0] if prices[0] <= prices[1] else 0
        best_income = [0, 0, second_income]
        for index in range(2, len(prices)):
            if prices[index] <= prices[index-1]:
                today_income = best_income[-1]
                best_income.append(today_income)
            else:
                if prices[index-1] >= prices[index-2]:
                    today_income = best_income[-1] + prices[index] - prices[index-1]
                    best_income.append(today_income)
                else:
                    today_income_1 = best_income[-3] + prices[index] - prices[index - 1]
                    unsure_value = 0 if (prices[index] - prices[index - 2]) <= 0 else (prices[index] - prices[index - 2])
                    today_income_2 = best_income[-2] + unsure_value
                    today_income = max(today_income_1, today_income_2)
                    best_income.append(today_income)

        return best_income[-1]


# leetcode_714  买卖股票的最佳时机含手续费 状态机的改变
class Solution_714:
    def maxProfit(self, prices, fee):
        if not prices or len(prices) <= 1:
            return 0

        cash, hold = 0, -prices[0]
        for index in range(1, len(prices)):
            cash = max(cash, hold + prices[index] - fee)        # 目前的现金（从0开始，也就是利润）
            hold = max(hold, cash - prices[index])              # 除去cash后剩余的钱（包括股票的钱） 可以为负
            print(prices[index], cash, hold)

        return cash


# demo = Solution_714()
# print(demo.maxProfit(prices=[1, 3, 2, 8, 4, 9, 5], fee=2)) #1 5 9  [1, 3, 2, 8, 4, 9]


# leetcode 121 买卖股票的最佳时机
class Solution_121:
    def maxProfit(self, prices):
        if not prices or len(prices) <= 1:
            return 0

        min_value, max_value, max_profit = prices[0], prices[0], 0
        for index in range(1, len(prices)):
            if prices[index] < min_value:
                min_value, max_value = prices[index], 0
            else:
                min_value = min(min_value, prices[index])
                max_value = max(max_value, prices[index])
                max_profit = max(max_profit, max_value - min_value)

        return max_profit


# demo = Solution_121()
# print(demo.maxProfit(prices=[7,6,4,3,1]))  #[7,1,5,3,6,4]  5


# leetcode 122 买卖股票的最佳时机 多次买卖
class Solution_122:
    def maxProfit(self, prices):
        if not prices or len(prices) <= 1:
            return 0

        cash, hold = 0, -prices[0]
        for index in range(1, len(prices)):
            cash = max(cash, hold + prices[index])        # 目前的现金（从0开始，也就是利润）
            hold = max(hold, cash - prices[index])        # 除去cash后剩余的钱（包括股票的钱） 可以为负
            print(prices[index], cash, hold)

        return cash


# demo = Solution_122()
# print(demo.maxProfit(prices=[7,1,5,3,6,4]))


# leetcode 714  买卖股票的最佳时机  最多完成K笔交易
class Solution_123:
    def maxProfit(self, prices):
        if not prices or len(prices) <= 1:
            return 0



# demo = Solution_122()
# print(demo.maxProfit(prices=[3,3,5,0,0,3,1,4])) [3,3,5,0,0,3,1,4]


# leetcode 303  求数组区域和
class NumArray:

    def __init__(self, nums):
        self.fix_list = nums

    def sumRange(self, i: int, j: int):
        return sum(self.fix_list[i:j+1])


# leetcode 530  二叉搜索树 任意两个节点的最小绝对差  中序遍历 从小到大的顺序排的
class TreeNode_530:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_530:
    def getMinimumDifference(self, root: TreeNode_530) -> int:
        if not root:
            return 0

        item_list, min_value = self.in_order(root=root), 9999999
        for i in range(0, len(item_list) - 1):
            min_value = min(min_value, item_list[i+1] - item_list[i])

        return min_value

    def in_order(self, root):
        if not root:
            return []

        return self.in_order(root.left) + [root.val] + self.in_order(root.right)


# LeetCode  669 修剪二叉搜索树   深度优先遍历
class TreeNode_669:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_669:
    def trimBST(self, root: TreeNode, L: int, R: int):
        if not root:
            return None

        if root.val < L:
            return self.trimBST(root=root.left, L=L, R=R)

        if root.val > R:
            return self.trimBST(root=root.right, L=L, R=R)

        if L <= root.val <= R:
            root.left = self.trimBST(root=root.left, L=L, R=R)
            root.right = self.trimBST(root=root.right, L=L, R=R)

        return root


# leetcode 538  把二叉搜索树转换为累加树  深度遍历 先右后左
class TreeNode_538:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_538:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.num = 0
        def convertBST_1(root):
            if not root:
                return

            convertBST_1(root=root.right)
            self.num += root.val
            root.val += self.num
            convertBST_1(root.left)
            return root

        return root


# leetcode 167 输入有序数组
class Solution_167:
    def twoSum(self, numbers, target):
        if not numbers:
            return []

        i, j = 0, len(numbers) - 1
        sign = 0
        while(i < j):
            if numbers[i] + numbers[j] == target:
                break
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1

        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        else:
            return []


# leetcode 633 平方数之和
class Solution_633:
    def judgeSquareSum(self, c: int) -> bool:

        import math
        i, j = 0, int(math.sqrt(c))
        print(j)
        while(i < j):
            if i * i + j * j == c:
                break
            if i * i + j * j < c:
                i += 1
            if i * i + j * j > c:
                j -= 1

        if i * i + j * j == c:
            return True
        else:
            return False


# leetcode 345  反转字符串中的元音字母
class Solution_345:
    def reverseVowels(self, s: str) -> str:
        str_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        demo_list = list(s)

        i, j = 0, len(demo_list) - 1
        while(i < j):
            if demo_list[i] in str_list and demo_list[j] in str_list:
                demo_list[i], demo_list[j] = demo_list[j], demo_list[i]
                i += 1
                j -= 1

            if demo_list[i] in str_list and demo_list[j] not in str_list:
                j -= 1

            if demo_list[i] not in str_list and demo_list[j] in str_list:
                i += 1

            if demo_list[i] not in str_list and demo_list[j] not in str_list:
                i += 1
                j -= 1

        return "".join(demo_list)


# leetcode 680   验证回文字符串 Ⅱ  跳过那个字符串就好了
class Solution_680:
    def validPalindrome(self, s: str):
        demo_list = list(s)
        i, j = 0, len(demo_list) - 1
        while (i < j):
            if demo_list[i] != demo_list[j]:
                break
            i, j = i + 1, j - 1

        return self.verify_str(temp_list=demo_list, i=i) or self.verify_str(temp_list=demo_list, i=j)

    def verify_str(self, temp_list, i):
        import copy
        s_list = copy.copy(temp_list)
        if not s_list:
            return True
        print(i, s_list)
        del s_list[i]
        i, j = 0, len(s_list) - 1
        while (i < j):
            if s_list[i] != s_list[j]:
                return False
            i, j = i + 1, j - 1

        return True


# LeetCode 88 合并两个有序数组  从后往前走
class Solution_88:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]


# leetcode 141 环形链表
class ListNode_141:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_141:
    def hasCycle(self, head: ListNode):
        if not head:
            return True

        slow, fast = head, head
        while(slow and fast):
            fast = fast.next.next if fast.next else None
            slow = slow.next
            if fast == slow:
                return True
        return False


# leetcode 451  根据字符出现频率排序
class Solution_451:
    def frequencySort(self, s: str):
        demo_list = list(s)
        demo_dic = {}
        for i in demo_list:
            if i in demo_dic:
                continue
            demo_dic[i] = demo_list.count(i)

        sort_list = sorted(demo_dic.items(), key=lambda x:x[1], reverse=True)
        result = ""
        for item in sort_list:
            demo_str, count = item
            result += demo_str * count

        return result


# leetcode 524 通过删除字母匹配到字典里最长单词  双指针
class Solution_524:
    def findLongestWord(self, s, d):
        max_str = ""
        pass


# leetcode 435 无重叠区间
class Solution_435:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x:x[0])
        last = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[last][1] > intervals[i][0]:
                if intervals[i][1] < intervals[last][1]:
                    last = i
                res += 1
            else:
                last = i
        return res


# demo = Solution_435()
# print(demo.eraseOverlapIntervals(intervals= [ [1,2], [2,3], [3,4], [1,3] ]))


# leetcode 46  全排列  给定一个没有重复数字的序列，返回其所有可能的全排列。 #利用dic进行一个判断key是否已经排过序
class Solution_46:
    result = []
    def permute(self, nums):
        self.result = []
        result_len = len(nums)
        self.handle_list(dic_order={}, new_nums=[], left_nums=nums, total=result_len)
        return self.result

    def handle_list(self, dic_order, new_nums=[], left_nums=[], total=0):
        if not left_nums or len(new_nums) == total:
            self.result.append(new_nums)

        for index, item in enumerate(left_nums):
            if item in dic_order:
                return self.handle_list(dic_order=dic_order,
                                        new_nums=new_nums,
                                        left_nums=left_nums[:index] + left_nums[index+1:],
                                        total=total)
            dic_order[item] = 1
            self.handle_list(dic_order=dic_order,
                             new_nums=new_nums + [item],
                             left_nums=left_nums[:index] + left_nums[index+1:],
                             total=total)
            dic_order.__delitem__(item)


# leetcode 47 全排列  给定一个有重复数字的序列，返回其所有可能的全排列  排序-然后判断前后是否相等
class Solution_47:
    result = []

    def permuteUnique(self, nums):
        if not nums: return []
        nums.sort()
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


demo = Solution_47()
print(demo.permuteUnique(nums=[1,2,1]))