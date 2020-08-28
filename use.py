def calc(numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum)

def calc(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum)
nums = [1,2,3]
calc(*nums)
calc(1,2,3,4)


# 传入一个list在函数内部对该list元素的操作会改变原始值
def exp(name, list):
    name = 'lwd'
    list[0] = 8
name = 'mts'
l = [1,2,3]
print(name, l)
exp(name, l)
print(name, l) 


# 可变参数
def product(*num):
    sum = 1
    for i in num:
        sum *= i
    return sum

## 传参时，前面加*表示把这个列表转换成可变参数
nums = [1,2,3,4]
product(*nums)


# 关键字参数
def person(name, age, **kw):
        print('name:', name, 'age:', age, 'other:', kw)

person('Micheal', 30)
person('Bob', 35, city='beijing')
person('wendy', 22, gender='M', city='beijing')

extra = {'job': 'pcb engineer', 'city': 'beijing'}
person('lwd', 22, **extra)



# 函数参数定义顺序：必选参数、默认参数、可变参数、关键字参数、命名关键字参数
def myfunction(name, age, gender, city = 'beijing', *arg, **argw, height, hobby = 'coding'):
    print(name, age, gender, city, arg, argw)

myfunction('lwd', 24, 'M', )

data1 = ['wendy', 20, 'M']
arg = [1,2,3]
argw = {'num1':1, 'num2':2}
myfunction(*data1)


# 递归
def fact(n):
    if n >= 2:
        return n*fact(n-1)
    else:
        return 1
# 尾递归
def facttail(num, res):   
    if num == 1:
        return res
    else:
        return facttail(num-1, res*num)





d = {}
for i in range(26):
    key = chr(0x61 + i)
    d[key] = i
for (k,v) in d.items():
    print('the value of %c is %d'%(k,v))
