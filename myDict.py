# -- myDict.py --

# 编写一个Dict类，用法和系统dict一致
# 增加 . 运算符功能
# 再谈__getattr__和__setattr__
## 当给一个对象使用.运算符时，就在调用__getattr__和__setattr__方法

## 当不重定义__getattr__方法时,执行obj.attr1, 调用父类默认的__getattr__方法，即__getattr__(obj, attr1)
## 默认方法会判断该属性是否存在，当attr1不存在，会返回AttributeError错误

## 在重定义__getattr__后，执行obj.attr1, 就会先检测obj有没有已经存在属性，然后调用自己的__getattr__方法，即__getattr__(obj, attr1)
## 执行完这个方法，obj.attr1语句也结束，返回值就是obj.attr1的值
## hasattr(obj, attr1)也会调用__getattr__方法，要是没有异常，则返回True
## 所以要是在__getattr__里只写pass，那么用hasattr检测任何属性都返回True
class Dict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        # 这里本来会返回keyError，将其转换成attributeError抛出
        ## 注：dict类型，key值不是其属性
        except KeyError:
            raise AttributeError("has no attribute %s"%attr)
    def __setattr__(self, attr, value):
        self[attr] = value
