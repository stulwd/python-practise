class Student(object):  #a empty class
    pass

s = Student()
s.name = 'lwd'

## 给一个对象绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  #attach set_age fun to instance set_age.

## 给某一个对象绑定方法后，其他同类对象不具备此方法
s2 = Student()
s2.set_age(25)      #it is invalid.

## 给类绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score   #attach set_score fun to class Student.

## 使用__slots__属性定义子对象可以定义的属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'lwd'
s.age = 25
s.score = 99 # invalid

## 父类定义的__slots__属性对于其子类没有影响
class Senior(Student):
    pass

s1 = Senior()
s1.score = 99 # 合法
s1.age = 32

## 在类中定义方法
## 参数检查
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

## 装饰器：将一个方法变成属性调用
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


## 多重mixIn继承
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# class Dog(Mammal):
#     pass

# class Bat(Mammal):
#     pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


class FlyableMixIn(object):
    def fly(self):
        print('flying...')

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass



