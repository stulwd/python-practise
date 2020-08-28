# 类的类型
class student(object):
    pass
type(student)

# 使用type创建类
def fn(self, name = 'world'):
    print('hello%s'%(name))
## 第一个参数是class的名称，第二个参数是继承类的组合，第三个参数是包含属性和方法的dict
Hello = type("Hello", (object,), dict(hello=fn))
h = Hello()
h.hello()
