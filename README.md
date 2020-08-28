## magic.py -- python之魔法
- __str__和__repr__魔法
- __iter__和__next__魔法、__getitem__魔法
- Iterable和Iterator
- 再议for循环
- __getitem__和__setitem__魔法与[]运算符
- __getattr__和__setattr__魔法与 . 运算符
- __call__魔法

## base.py -- python之入门
- 字符串不转义如何表示
- 字符编码
- unicode 和 utf-8
- 编解码方法
- 查看字符对应的编码
- 查看编码对应的字符
- 数字的进制表示法
- 进制转换
- list方法:insert append pop
- input用法
- dict方法：get pop
- set: add方法和remove方法
- 切片slice

## use.py -- python之使用
- 可变参数
- 关键字参数
- 函数参数定义顺序
- 递归
- 尾递归

## essential.py -- python之必要
- 字符串截取
- 列表生成式
- 生成器
- Iterable对象

## advanced.py -- python之高阶
- 高阶函数
- map映射
- reduce方法
- map和reduce组合用法
- lambda表达式
- 过滤器filter
- 装饰器decorator
- 高阶装饰器
- sorted()排序
- 闭包

## enumClass.py -- python之枚举
- Enum方法
- 继承Enum类

## obj.py -- python之类与对象
- 类的定义、构造函数
- 构造对象
- pass关键字
- __PropName私有属性
- 继承
- 方法重定义
- hasattr、setattr、getattr用法
- 类自己的属性

## advobj.py -- python类之进阶
- 使用MethodType给对象单独绑定方法
- 给某一个对象绑定方法后，其他同类对象不具备此方法
- 给类单独绑定方法
- 使用__slots__属性定义子对象可以定义的属性
- 父类定义的__slots__属性对于其子类没有影响
- 参数检查
- 装饰器：将一个方法变成属性调用
- 多重mixIn继承

## brim.py --python之边缘
- python脚本传入参数
- __name__值
- 变量函数定义规范：外部不需要引用的变量或函数定义为__fun或__property,公开的不要加__

## debug.py --python之错误与调试
- 为什么要处理错误
- try...except..finally
- 跨层抛出错误
- 子类错误被父类错误捕获
- 调用栈
- 记录错误logging
- 使用logging.exception()打印错误的调用栈
- 自定义错误类型
- 抛出自定义的错误
- 捕获自定义错误
- 在except处使用raise继续抛出错误
- 在except里使用raise转换成其他错误类型抛出
- 断言
- 屏蔽断言
- logging等级

## myDict.py、myDict_test.py --python之单元测试
- 再谈__getattr__和__setattr__
- unittest模块
- 继承测试类unittest.TestCase
- setUp和tearDown方法
- 如何运行单元测试

## myDict2.py --python之文档测试
