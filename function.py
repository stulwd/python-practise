#higher-order function
def abs_add(x, y, abs):
    return abs(x) + abs(y)


#map function
def f(x):
    return x**2

r = map(f, [1,2,3,4,5,6,7,8,9])
list(r)

list(map(str, [1,2,3,4,5]))


#reduce function
from functools import reduce
def fn(x, y):
    return x*10 + y

reduce(fn, [1,2,3,4,5])

def str2int(str):
    def chr2num(chr):
        a = {'1':1, '2':2, '3':3, '4':4,\
        '5':5, '6':6, '7':7, '8':8, '9':9, '0':0 }
        return a[chr]
    def fn(x,y):
        return x*10 + y
    return reduce(fn, map(chr2num,str))

def str2int(str):
    def chr2num(chr):
        a = {'1':1, '2':2, '3':3, '4':4,\
        '5':5, '6':6, '7':7, '8':8, '9':9, '0':0 }
        return a[chr]
    
    return reduce(lambda x,y : x*10 + y, map(chr2num,str))


def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

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



#filter
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1,2,3,4,5,6]))

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A','','B',None, 'C',' ']))

def prime(lim):
    a = [x for x in range(2,lim+1)]
    def delnp(num):
        

#define a odd sequence.
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



#sort
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sortregu1(tup):
    return tup[0].lower()

def sortregu2(tup):
    return tup[1]
sorted(L, key = sortregu)


#closure
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


#decorator 
def now():
    print('2018-09-19')

f = now

def log(func):
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-09-19')