class Student(object):  #a empty class
    pass
s = Student()
s.name = 'lwd'

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  #attach set_age fun to instance set_age.

s2 = Student()
s2.set_age(25)      #it is invalid.

def set_score(self, score):
    self.score = score

Student.set_score = set_score   #attach set_score fun to class Student.

#use __slot__
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'lwd'
s.age = 25
s.score = 99


class Senior(Student):
    __slots__ = ('score')
    pass


s1 = Senior()
s1.score = 99
s1.age = 32


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


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


#multiple inherit
class Animal(object):
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#各种动物：
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(pbjet):
    def run(self)：
        print('Running...')

class Flyable(object):
    def fly(self):
        print('flying...')

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass


#定制类
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'student object (name: %s)'%self.name
print(Student('lwd'))
