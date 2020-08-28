# python之魔法方法

## __str__和__repr__魔法
## 如果一个类中定义了该方法，则在print()或直接敲击对象时就会执行__str__和__repr__方法里定义的内容
class Student(object):
    '''
    __str__()是在print时调用的方法，重定义实现打印所需要的格式，类似C++的<<运算符重载
    __repr__()是直接敲变量，打印出来的东西
    operator<<(istream in, Student stu){
        in << stu.name
        return in;
    }
    '''
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'student object (name: %s)'%self.name
    __repr__ = __str__    
s1 = Student('lwd')
## 这里调用了__str__()方法
print(s1)
## 这里调用了__repr__()方法
s1


















# __iter__和__next__魔法、__getitem__和__setitem__魔法
## 可迭代类型和迭代器：
## Iterable有__iter__()方法，此方法功能是生成一个Iterator
## list、tuple、set、dict都是Iterable
## Iterator有__iter__()和__next__()方法，__iter__()返回的就是self，__next__()是迭代函数，返回下一个值

## 如果一个类定义了__iter__()，其实例对象就是Iterable类型了
## 如果同时还定义了__next__(), 其实例对象就是Iterator类型了
class fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1
    ## __iter__该方法使该类变为一个Iterable类型
    ## 并且此方法要返回一个Iterator，当该类没有定义__next__()方法时，说明该类不是一个Iterator
    ## 所以不要返回self，因为__iter__()目的就是要返回一个Iterator的
    ## 当定义了__next__时，就要返回self
    def __iter__(self): 
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    # 当没有__next__()方法时，是Iterable而非Iterator，在__iter__中必须返回其他的迭代器
    # def __iter__(self):
    #     return iter([1,2,3,4])

    # __getitem__魔法,类似于C++的[]运算符重载
    def __getitem__(self, n):
        f = fib()
        # 当中括号里时int时
        if isinstance(n, int):
            for i in range(n-1):
                f.__next__()
            return f.__next__()
        # 当中括号里时slice时
        if isinstance(n, slice):
            l = []
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            for i in range(start):
                f.__next__()
            for i in range(stop-start):
                l.append(f.__next__())
            return l
    # __setitem__魔法接收三个参数，当执行f[n] = value时，会调用这个方法
    def __setitem__(self, n, value):
        pass


f = fib()
## 判断f类型
from collections.abc import Iterable,Iterator
isinstance(f, Iterable) ## True
isinstance(f, Iterator) ## True
## 用next进行迭代
next(f)
next(f)

# 再议for循环：
# for循环内部逻辑
## 以for a in A为例：
## 首先用isinstance()判断A的类型是否为Iterable
## 当为Iterable时，则调用其__iter__()方法，将其创建为一个Iterator
##     1.先执行itr=A.__iter__()其构造为一个Iterator
##     2.每次循环时令a=itr.__next__()
##     3.循环体该怎么处理就怎么处理
##     注：要是A本来就是一个Iterator时，也会调用__iter__()，不过返回的依然是self，所以不影响

for item in fib():
    print(item)


f = fib()
# __getitem__魔法,下列用法会调用此魔法
f[3]
f[2]
f[:4]
f[1:10]
# 类似的还有__setitem__魔法，赋值时会调用此魔法
f[5] = 6

















# __getattr__和__call__魔法
class Student(object):
    def __init__(self, name='无名氏'):
        self.name = name
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)
## __getattr__实现链式调用
class Chain(object):
    def __init__(self, path=''):
        self.path = path
    def __str__(self):
        return self.path
    def __getattr__(self, path):
        return Chain("%s/%s" %(self.path, path) )
    # def users(self, name):
    #     return Chain("%s/%s" %(self.path, name) )
    def __call__(self, path):
        return Chain("%s/%s" %(self.path, path) )
    __repr__ = __str__

Chain().usr1.user('lwd').test.full_build
## 用callable可以检测对象本身是否可调用,只要定义了__call__()方法，则该对象一定是callable
callable(Chain) ## True
