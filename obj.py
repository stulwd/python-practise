std1 = {'name': 'Micheal', 'score': 98}
std2 = {'name': 'Bob', 'score':81}

def print_score(std):
    print("%s : %s"%(std['name'], std['score']))


# 类的定义、构造函数
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s'%(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C' 

# 构造对象
bart = Student('Bart Simpson', 59)
bart.print_score()

# pass关键字
class Student(object):
    pass

bart = Student()
bart.name = 'bart Simpson'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

# 形如'__PropName'类型的属性，不能在外部直接访问，要用obj._ClassName__PropName来访问
class Student(object):

    def __init__(self, name, sex, score):
        self.__name = name
        self.__score = score
        self.sex = sex

    def print_score(self):
        print('%s : %s'%(self.__name, self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            ValueError('bad score')

bart = Student('Bart Simple', 59)
bart.__name
bart._Student__name


# 继承
class Animal(object):
    def run(self):
        print('Animal is runing...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()


class Animal(object):
    def run(self):
        print('Animal is runing...')

class Dog(Animal):
    pass


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())

# 方法重定义
class Tortoise(Animal):
    def run(self):
        print('Tortoise is runing slowly...')

run_twice(Tortoise())



def fn():
    pass


a = str('abc')   #a is a instance of class str.
a.__len__()      #__len__ is a function of class str.
def mylen(str):                 #creat a function to show the length of string.
    return str.__len__()
a.lower()
a.upper()

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x *self.x

obj = MyObject()

# hasattr、setattr、getattr用法
hasattr(obj, 'x')
hasattr(obj, 'y')
setattr(obj, 'y', 19)
hasattr(obj, 'y')
getattr(obj ,'y')


class Student(object):      #the attr name belong to class Student
    name = 'Student'

# 类自己的属性
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')





