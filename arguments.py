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

#keyword arguments
def person(name, age, **kw):
        print('name:', name, 'age:', age, 'other:', kw)

person('Micheal', 30)
person('Bob', 35, city='beijing')
person('wendy', 22, gender='M', city='beijing')

extra = {'job': 'pcb engineer', 'city': 'beijing'}
person('lwd', 22, **extra) #have no influence to extern dict extra.

def exp(name, list):
    name = 'lwd'
    list[0] = 8
name = 'mts'
l = [1,2,3]
print(name, l)
exp(name, l) #change the value of l.
print(name, l) 


def product(*num):
    sum = 1
    for i in num:
        sum *= i
    return sum

def myfunction(name, age, gender, city = 'beijing', *arg, **argw):
    print(name, age, gender, city, arg, argw)

data1 = ['wendy', 20, 'M']
arg = [1,2,3]
argw = {'num1':1, 'num2':2}
myfunction(*data1)


def fact(n):
    if n >= 2:
        return n*fact(n-1)
    else:
        return 1

def facttail(num, res):   #optimization the problem of stack overflow: means res * num!
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