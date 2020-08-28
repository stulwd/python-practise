# 字符串截取
def trim(obj):
    if obj == '':
        return ''
    rear = obj[0]
    while rear == ' ':
        obj = obj[1:]
        if len(obj) != 0:
            rear = obj[0]
        else:
            return ''

    tail = obj[-1]
    while tail == ' ':
        obj = obj[0:-1]
        tail = obj[-1]

    return obj


# 字符串截取测试
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

# 列表生成式
[x*x for x in range(10)]
[x*x for x in range(10) if x%2 == 0]
[m+n for m in 'ABC' for n in 'XYZ']
import os
[d for d in os.listdir('.')]

d = {'x':'a', 'y':'b', 'z':'c'}
for k,v in d.items():
    print(k, '=', v)

#transfer the string to captial.
L1 = ['Hello', 'World', 18, 'Apple', None]
#delete the elements that aren't string.
L2 = [s.lower() for s in L1 if isinstance(s, str)]
#reserve the other type.
L2 = [s.lower() if isinstance(s, str) else s for s in L1] 


# 生成器
# for语句的循环范围必须是Iterable类型
g = (x*x for x in range(10))
next(g)

for n in g:
    print(n)

def fib(m,n,limit):
    print(m+n)
    if n+m+n < limit :
        fib(n,m+n,limit)

# Iterable对象
from collections import Iterable
isinstance([], Iterable)
isinstance([], Iterable)
isinstance((x for x in range(10)), Iterable)

from collections import Iterator
isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)
isinstance({}, Iterator)

x_iter = iter([x**2 for x in range(10)])
