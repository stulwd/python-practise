# 高阶函数
def abs_add(x, y, abs):
    return abs(x) + abs(y)


# 映射方法
def f(x):
    return x**2

r = map(f, [1,2,3,4,5,6,7,8,9])
list(r)

list(map(str, [1,2,3,4,5]))


# reduce方法
from functools import reduce
def fn(x, y):
    return x*10 + y

reduce(fn, [1,2,3,4,5])

# map和reduce组合用法
def str2int(str):
    def chr2num(chr):
        a = {'1':1, '2':2, '3':3, '4':4,\
        '5':5, '6':6, '7':7, '8':8, '9':9, '0':0 }
        return a[chr]
    def fn(x,y):
        return x*10 + y
    return reduce(fn, map(chr2num,str))

## lambda表达式用法
def str2int(str):
    def chr2num(chr):
        a = {'1':1, '2':2, '3':3, '4':4,\
        '5':5, '6':6, '7':7, '8':8, '9':9, '0':0 }
        return a[chr]
    
    return reduce(lambda x,y : x*10 + y, map(chr2num,str))

## 字符串数组每个元素首字母大写
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

## 数组中的所有元素相乘
def prod(L):
    import functools
    return reduce(lambda x,y:x*y , L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



def str2float(s):

    s1 = s[:s.find('.')] + s[s.find('.')+1:]
    pd = s[::-1].find('.')
    def chr2num(c):
        a = {}
        for i in range(10):
            a[chr(0x30+i)] = i
        return a[c]
    return 10**(-pd)*reduce(lambda x,y:10*x+y , map(chr2num, s1))
    
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



# 过滤器
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1,2,3,4,5,6]))

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A','','B',None, 'C',' ']))

def prime(lim):
    a = [x for x in range(2,lim+1)]
    def delnp(num):
        

# define a odd sequence.
def _odd_iter()
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def is_palindrome(n):
    return str(n) == str(n)[::-1]



# sort
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sortregu1(tup):
    return tup[0].lower()

def sortregu2(tup):
    return tup[1]
# key指定一个函数fun，每个元素会按照map(fun, L)映射的结果来排序
# reverse指定反向排序
sorted(L, key = sortregu, reverse = True)


#closure   
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


# 装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper
## 相当于执行了now=log(now)=wrapper语句
@log
def now():
    print('2018-09-19')    


# 高阶装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('call %s():'% func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
## 相当于执行了log('execute'),返回decorator函数，然后执行decorator(log)
@log('execute')
def now():
    print('2015-3-25')
## now=log('execute')(log)=decorator(log)=wrapper
## now()=wrapper()=print,log()

# Hanno Tower
def move(n, a, b, c):
    if n == 1:
        print(a,'>>', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

def cal(num, s=1):
    if num == 1:
        return s
    else:
        return cal(num-1, 2*s+1)

a = [[0 for i in range(8)] for i in range(8)]
b = [0 for i in range(8)]
method = 0
def add(x, y):
    b[x] = y
    for i in range(8):
        for j in range(8):
            if i == x or j == y or i+j == x+y or x-i == y-j:
                a[i][j] += 1
def clear(x, y):
    for i in range(8):
        for j in range(8):
            if i == x or j == y or i+j == x+y or x-i == y-j:
                a[i][j] -= 1
def queen(colum):
    global method
    for i in range(8):
        if a[colum][i] == 0:
            add(colum, i)
            if colum <= 6:
                queen(colum+1)
            else:
                print(b)
                method += 1
            clear(colum, i)
queen(0)
print('total method:%d'%method)

def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur+1)
queen([None]*8)
