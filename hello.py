'a test module'

__author__ = 'lwd'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
else:
    print('hello module!')


def __private_1(name):
    return 'hello, %s'% name


def __private_2(name):
    return 'hi, %s'% name

def greeting(name):
    if len(name) > 3:
        return __private_1(name)
    else:
        return __private_2(name)