import time
import functools
import numbers

# 装饰器在Python加载模块时立即运行  框架外面包着route
registry = []


def register(func):
    print('running register %s' % func)
    registry.append(func)
    return func


@register
def f1():
    print("i am f1")

#
# if __name__ == '__main__':
#     f1()


b = 6


def f2(a):
    global b
    print(a, b)
    b = 5   # UnboundLocalError: local variable 'b' referenced before assignment
    print(b, '==')


f2(4)

# 闭包


def make_averager():
    total, count = 0, 0

    def averager(new_value):
        nonlocal count, total   # 将变量标记为自由变量
        count += 1      # 想修改total和count的值不可以 因为他们是不可变对象(数字 字符串 元组) 如果是list dict类型就可以
        total += new_value
        return new_value / count

    return averager


a = make_averager()
print(a(3))


def clock(func):
    """输出函数的运行时间"""
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.9fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))       # %fs是两个东西，%f指浮点型，s指秒（seconds）0.8小数点后8位
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


snooze(.123)


# 优化后的装饰器


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))

        arg_str = ', '.join(arg_list)
        print('[%0.9fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@functools.lru_cache()      # 把耗时的函数的结果保存起来
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(30))


# 单分派泛函数 装饰器可以把整体方案拆分成多块
@functools.singledispatch
def sort_type(obj):
    print(obj, type(obj), 'obj')


@sort_type.register(str)
def _(text):
    print(text, type(text), 'text')


@sort_type.register(numbers.Integral)
def _(n):
    print(n, type(n), 'int')


sort_type('aaaa')
sort_type(123)


