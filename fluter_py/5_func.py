import random
import bobo
import inspect

from operator import itemgetter, attrgetter
from collections import namedtuple
from functools import partial


def factorial(n):
    """func notes"""
    print(n, "===")
    return 1 if n < 2 else n * factorial(n - 1)


#print(factorial(5))
print(factorial.__doc__)
print(type(factorial))
#demo = map(factorial, range(11))
#print(list(demo))

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'bannana']
print('testing'[::-1])

print(list(map(factorial, range(1, 4))))        #   执行factorial函数6次
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))

# filter func and map func return iterator


class BingoCage(object):

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)     # 洗牌 重新定义列表顺序

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self, *args, **kwargs):
        return self.pick()

    def print_items(self):
        return self._items


demo = BingoCage(range(3))
print(demo.pick())
print(demo())
print(demo.print_items())


# func 关键字参数
def tag(name, *content, cls=None, **attrs):
    """生成一个或者多个HTML标签"""
    if cls:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s" ' % (attr, value)
                           for attr, value in sorted(attrs.items())
                           )
    else:
        attr_str = ""

    if content:
        return "\n".join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content
                         )
    else:
        return '<%s%s /> ' % (name, attr_str)


print(tag('br'))
print(tag('br', 'hello', 'world'))      #   第一个参数后面的任意个参数会被*content捕获 存入元祖
print(tag('p', 'hello', id=33))
print(tag(**{'name': 'img', 'title': "Sunset", "src": "sunset.jpg", 'cls': "framed", 'content': 123}))


@bobo.query('/')
def hello(person):
    return 'hello {person}!'.format(person=person)


a = tag('img', 'good')

sig = inspect.signature(tag)    # 解释参数对应到哪个位置
my_tag = {"name": "img", "title": "SUNSET", "src": 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
for name, value in bound_args.arguments.items():
    print(name, '==', value)


metro_data = [
    ('Tokyo', 'JP', 36.933),
    ('Delhi', 'IN', 321.935),
    ('NEXICO', 'MX', 20.142),
    ('PAULO', 'BR', 19.649),
]


for city in sorted(metro_data, key=itemgetter(1)):  # 根据元组第二个元素进行排序
    print(city)


Metropolis = namedtuple('Metropolis', 'name cc pop')
metro_areas = [Metropolis(name, cc, pop) for name, cc, pop in metro_data]

name_pop = attrgetter('name', 'pop')
for city in sorted(metro_areas, key=attrgetter('pop')):
    print(name_pop(city))


pic = partial(tag, 'img', cls='pic')    # 返回一个partial对象
print(pic(src="a.jpg"))
