std1 = {'name': 'Micheal', 'score': 98}
std2 = {'name': 'Bob', 'score':81}

def print_score(std):
    print("%s : %s"%(std['name'], std['score']))



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


bart = Student('Bart Simpson', 59)
bart.print_score()


class Student(object):
    pass

bart = Student()
bart.name = 'bart Simpson'
bart.name

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

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
