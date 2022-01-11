"""
Description

RSA加密算法是一种非对称加密算法，它在1977年被提出，是一种可以用于数据加密或数字签名的算法，至今仍在使用。
RSA的安全性依赖于大数分解，所以模数 n 一般取得较大。一般我们选取两个素数 p 和 q ，模数 n=p*q
选取 e 作为加密密钥，m 为明文消息，则密文消息 c=m^e mod n.
欧拉函数 phi(n)=(p-1)*(q-1)，解密秘钥为d, e*d=1 mod phi(n) ，明文消息就可以通过 m=c^d mod n得到。
某次CTF比赛中师傅们得到了好多由同一个模数 n(23333 * 10007)加密的密文，但是每次的 ee 都不一样，师傅们希望你能根据不一样的 ee 去解密出密文消息。

Input
一行包含两个整数 e(3<= e <= phi(n)) 和 c(0 ≤ c ≤ n)

Output
一行包含 m

Sample Input 1
3 123612763
Sample Output 1
84859100
Hint

由 e=3 可以求出 d=155639995, m=c^d=84859100
"""


def get_prev_num(e):
    n = 23333 * 10007
    pass


"""
Description

公司终于安好饮水机了，monster 迫不及待要去接水，但是他到那里才发现前面已经有n个同事了。他数了数，饮水机一共有m个接水口。
所有的同事严格按照先来后到去接水（m个接水口同时工作，哪个水龙头有空人们就去哪里，如果 n < m，那么就只有n个接水口工作）。
每个人都有一个接水的时间，当一个人接完水后，另一个人马上去接，不会浪费时间。monster 着急要开会，所以他想知道什么时候才能轮到他。

Input
第一行两个整数n和m，表示 monster 前面有n个人，饮水机有m个接水口。n, m <1100。第二行n个整数，表示每个同学的接水时间。

Output
"""


def get_left_time(n, m, cost_list):
    if n < m:
        return 0

    curr_time_list = [0] * m
    cost_time = 0
    for cost in cost_list:
        min_curr_time = min(curr_time_list)
        cost_time += min_curr_time
        has_changed = False
        for index in range(len(curr_time_list)):
            curr_time_list[index] -= min_curr_time
            if not has_changed and curr_time_list[index] == 0:
                curr_time_list[index] = cost
                has_changed = True

    return cost_time + min(curr_time_list)


print(get_left_time(4, 2, [1, 1, 1, 1]))


"""
整除的
"""


def get_mod_num(arr_len, arr_list):
    result = 0
    one_num, two_num = 0, 0
    for i in range(arr_len):
        arr_list[i] = int(arr_list[i]) % 3
        if arr_list[i] == 0:
            result += 1
        if arr_list[i] == 1:
            one_num += 1
        if arr_list[i] == 2:
            two_num += 1

    result += min(one_num, two_num)
    result += abs(one_num - two_num) // 3

    print(result)
    return result


"""
base64 解码  + 转36进制
"""


import base64


def get_base36(transfer_str):
    temp = base64.b64decode(transfer_str).decode()
    print(temp)


get_base36("cGFzc3dvcmQgaXMgQWRtaW4xMjM0NTY=")
print("password is Admin123456".encode(encoding="utf-8").decode(encoding="utf-8"))


"""
安全团队
"""


def get_small_cost(own_cost, together_cost):
    all_cost = 0
    chart_list = []
    together_cost_dict = {}
    for item in together_cost:
        business_a, business_b, curr_cost = item
        business_a, business_b = (business_b, business_a) if business_b < business_a else (business_a, business_b)
        together_cost_dict[(business_a, business_b)] = min(together_cost_dict.get((business_a, business_b), 0), curr_cost)

    for key, value in together_cost_dict.items():
        business_a, business_b = key
        in_chart = False
        for index, chart in enumerate(chart_list):
            conn_list, chart_cost = chart
            conn_list = list(set(conn_list + [business_a, business_b]))
            min_cost = 0
            if business_a in conn_list and business_b not in conn_list:
                min_cost = min(
                    chart_cost,
                    curr_cost + min(own_cost[business_a - 1], own_cost[business_b - 1])
                )

        if not in_chart:
            min_cost = value + min(own_cost[business_a - 1] + own_cost[business_b - 1],
                                   value + min(own_cost[business_a - 1] + own_cost[business_b - 1])
                                )
            chart_list.append(([business_b, business_a], min_cost))

    for chart in chart_list:
        conn_list, chart_cost = chart
        all_cost += chart_cost

    print(all_cost)


# get_small_cost([100, 100], [(1, 2, 1000)])


"""
斐波那契数列
"""


def fib_print(n, fib_dic):
    if fib_dic.get(n):
        return fib_dic.get(n), fib_dic

    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_print(n - 1, fib_dic)[0] + fib_print(n - 2, fib_dic)[0]

    fib_dic[n] = result
    return result, fib_dic


def get_input_data():
    import sys
    fib_dic = {1: 1, 2: 1}
    while True:
        line_data = sys.stdin.readline().strip()
        result, fib_dic = fib_print(int(line_data), fib_dic)
        print(result)
        if int(line_data) >= sys.maxsize:
            break


# get_input_data()


"""
处理问题
"""


def get_customer_num(customer_list, tech_list):
    customer_list.sort()
    tech_list.sort()

    result = 0
    skill_curr = 0
    for need_skill in customer_list:
        for skill_index in range(skill_curr, len(tech_list)):
            if tech_list[skill_index] >= need_skill:
                result += 1
                skill_curr += 1
                break

    return result


print(get_customer_num([5, 7, 9], [3, 3, 5, 3, 3]))


"""
日志处理
"""


def insert_data(log_list, log_len, insert_value, front=False):
    if not log_list:
        return 0, [insert_value]

    if insert_value > log_list[-1]:
        return log_len, log_list + [insert_value]

    l, r = 0, log_len - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if log_list[mid] >= insert_value:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1

    while front and log_list[ans] == insert_value:
        ans -= 1

    if front and log_list[ans] < insert_value:
        ans += 1

    while not front and log_list[ans] == insert_value:
        ans += 1

    return ans, log_list[:ans] + [insert_value] + log_list[ans:]


print(insert_data([
    1564900000,
    1564900005,
    1564900008,
    1564900007,
    1564900009
], 5, 1564900005, False))


print("-====")
# print(insert_data([1,2,3,3,3,6,7], 5, 3, True))


def get_input_data():
    import sys
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        access_log = []
        line_count = sys.stdin.readline().strip()
        for i in range(int(line_count)):
            log_time = sys.stdin.readline().strip()
            _, access_log = insert_data(access_log, i, int(log_time))

        output_count = sys.stdin.readline().strip()
        for i in range(int(output_count)):
            start_time, end_time = sys.stdin.readline().strip(' ').replace("\n", "").split(' ')
            start_index, _ = insert_data(access_log, int(line_count), int(start_time), True)
            end_index, _ = insert_data(access_log, int(line_count), int(end_time), False)
            print(start_index, end_index, _)
            print(end_index - start_index)

# get_input_data()

"""
爬虫算法
"""


def get_min_time(n, p, cost_list, link_list):
    pass


"""
攻防演练
"""


def get_min_jump(target_list, jump_list, target, curr=1):
    """
    target_list: [1,2,3,4,5,6]
    jump_list: [(1,2),(2,3),(3,4)]
    """
    target_set = set(sorted(target_list))
    jump_list = sorted(jump_list, key=lambda x: x[0])
    curr = 1
    result = 0
    conn_set = ()
    for item in target_set:
        pass



def find_path(curr, target, jump_list):
    tmp = (min(curr, target), max(curr, target))
    if tmp in jump_list:
        return 1

    return 0


def get_left_time(n, m, cost_list):
    if n < m:
        return 0

    curr_time_list = [0] * m
    cost_time = 0
    for cost in cost_list:
        cost = int(cost)
        min_curr_time = min(curr_time_list)
        cost_time += min_curr_time
        has_changed = False
        for index in range(len(curr_time_list)):
            curr_time_list[index] -= min_curr_time
            if not has_changed and curr_time_list[index] == 0:
                curr_time_list[index] = cost
                has_changed = True

    return cost_time + min(curr_time_list)


def get_input_data1():
    import sys
    n, m = sys.stdin.readline().strip(' ').replace("\n", "").split(' ')
    list_demo = sys.stdin.readline().strip(' ').replace("\n", "").split(' ')
    result = get_left_time(int(n), int(m), list_demo)
    print(result)


def get_customer_num(customer_list, tech_list):
    customer_list = [int(i) for i in customer_list]
    tech_list = [int(i) for i in tech_list]

    customer_list.sort()
    tech_list.sort()

    result = 0
    skill_curr = 0
    for need_skill in customer_list:
        for skill_index in range(skill_curr, len(tech_list)):
            if int(tech_list[skill_index]) >= need_skill:
                result += 1
                skill_curr += 1
                break

    return result


def get_input_data():
    import sys
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        n, k = sys.stdin.readline().strip(' ').replace("\n", "").split(' ')
        need_skill_list = sys.stdin.readline().strip(' ').replace("\n", "").split(' ')
        have_skill_list = sys.stdin.readline().strip(' ').replace("\n", "").split(' ')
        result = get_customer_num(need_skill_list, have_skill_list)
        print(result)

get_input_data()