import os
from multiprocessing import Process


def f(name):
    print("子", os.getpid())
    print('hello', name)


# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
#
#     print("父", os.getpid())


class Test(object):

    def test_1(self):
        pass

    @classmethod
    def test_2(cls):
        pass

    @staticmethod
    def test_3():
        pass


def wrap(func):
    print("wrap")
    return func

@wrap
def test_1():
    print("test_1")


@wrap
def test_2():
    print("test_2")

#
# test_1()
# test_2()


async def test_gen_sort():
    await asyncio.sleep(2)
    print("=====2")
    return {"sort": 1}


async def test2_gen_sort():
    await asyncio.sleep(2)
    print("=====3--2")
    return {"sort": 2}


async def all():
    dic1 = await test_gen_sort()
    print("======dic1")
    dic2 = await test2_gen_sort()
    print("======dic2")
    demo = dic1.get('sort') + dic2.get('sort')
    print("demo===", demo)
    return demo

import time
import asyncio
print(time.time())
# loop = asyncio.get_event_loop()
# task = [asyncio.ensure_future(test_gen_sort()), asyncio.ensure_future(test2_gen_sort()), asyncio.ensure_future(all())]
# loop.run_until_complete(asyncio.wait(task))
# print(time.time())


import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()
    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance
    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount, xx):
        # 加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self._balance >= draw_amount:
                # 吐出钞票
                time.sleep(xx)
                print(threading.current_thread().name\
                    + "取钱成功！吐出钞票:" + str(draw_amount), "xx:", xx)
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为: " + str(self._balance))
            else:
                print(threading.current_thread().name\
                    + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()

def draw(account, draw_amount, xx):
    # 直接调用account对象的draw()方法来执行取钱操作
    account.draw(draw_amount, xx)
# 创建一个账户
acct = Account("1234567" , 1000)
# 模拟两个线程对同一个账户取钱
# threading.Thread(name='甲', target=draw , args=(acct , 800, 2)).start()
# threading.Thread(name='乙', target=draw , args=(acct , 800, 1)).start()


loop = asyncio.get_event_loop()

async def test_as():
    asyncio.wait([
        loop.create_task(test_gen_sort()),
        loop.create_task(test2_gen_sort()),
    ])
    await test_gen_sort()
    await test2_gen_sort()

import time
import asyncio
print(time.time())
task = [asyncio.ensure_future(test_as())]
loop.run_until_complete(asyncio.wait(task))
print(time.time())