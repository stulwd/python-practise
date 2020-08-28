# 程序运行时，要是出现错误必须要处理，要不然会因为各种问题退出
# 用错误码来表示是否出错不方便，因为要一级一级上报，直到能处理该错误

# try...except..finally
try:
    print('try...')
    # r = 10 / 0
    r = 10 / 'a'
    # r = 10 / int('a')
    print(r)
except ZeroDivisionError as e:
    print('ZeroDivisionError...', e)
except TypeError as e:
    print('TypeError...', e)
except ValueError as e:
    print('ValueError...', e)
else:
    print('no error')
finally:
    print('finally...')


# 跨层抛出错误
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)*2

try:
    print('try...')
    bar('0')
except ZeroDivisionError as e:
    print('ZeroDivisionError ', e)
finally:
    print('finished...')

# 子类错误被父类错误捕获
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)*2

try:
    '''some code'''
except ValueError as e:
    print('ValueError ', e)
## UnicodeError不会被捕获
except UnicodeError as e:
    print('UnicodeError... ', e)
finally:
    print('finished...')

# 调用栈
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)*2

bar('a')

# 记录错误logging
## 使用logging.exception()打印错误的调用栈
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)*2

try:
    print('try...')
    bar('0')
except ZeroDivisionError as e:
    print(e)
    logging.exception(e)
finally:
    print('finished...')

print('hello world')


# 自定义错误类型
class FooError(ValueError):
    pass
# 抛出自定义的错误
def fun():
    raise FooError('invalid value:')
    print('hello world')
fun()

# 捕获自定义错误
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value:%s'%s)
    return 10/n
try:
    foo(0)
except FooError as e:
    logging.exception(e)
finally:
    print('finished')

# 在except处使用raise继续抛出错误
try:
    i = 10 / 0
except ZeroDivisionError as e:
    print('处理不了除0错误，继续网上抛出',e)
    raise
finally:
    print('finished')

# 在except里使用raise转换成其他错误类型抛出
try:
    i = 10 / 0
except ZeroDivisionError:
    raise ValueError('incorrect Value')
finally:
    print('finished')


# 断言
# 当脚本运行时，加上-O参数就可以关闭所有断言(相当于注释了所有断言行):python -O test.py
def fun(s):
    # 要是断言失败，就会抛出AssertionError,传入后面的文字，相当于raise AssertionError('invalid arg')
    assert isinstance(s, int) and s != 0, 'invalid arg'
    return 10 / s
fun(3)

# logging
import logging
# logging的等级分为 debug < info < warning < error
# 设置logging的最低等级，之后等级低于设定等级的logging将不会输出
logging.basicConfig(level=logging.DEBUG)
# 因为设定了最低等级是warning，所以会忽略debug和info
logging.debug('debug')
logging.info('some info')
logging.warning('warn: ...')
logging.error('error happend')
# 交互模式下显示的信息：warning  error
# 脚本模式下显示的信息：所有
