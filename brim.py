'a test module'

__author__ = 'lwd'

import sys

# python脚本传入参数
def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# __name__值:当作为主进程运行时，为__main__
#            当作为子进程运行时，为__模块名__
if __name__ == '__main__':
    test()
else:
    print('hello module!')


# 外部不需要引用的变量或函数定义为__fun或__property,公开的不要加__
def __private_1(name):
    return 'hello, %s'% name


def __private_2(name):
    return 'hi, %s'% name

def greeting(name):
    if len(name) > 3:
        return __private_1(name)
    else:
        return __private_2(name)
