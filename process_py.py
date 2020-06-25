import os
from multiprocessing import Process


def f(name):
    print("子", os.getpid())
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

    print("父", os.getpid())


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


test_1()
test_2()