# -- myDict.py --

# 文档测试,将期望的输出用''' '''包含
class Dict(dict):
    '''
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y
    Traceback (most recent call last):
        ...
    KeyError: 'y'
        ...
    Traceback (most recent call last):
        ...
    AttributeError: has no attribute y
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
        ...
    Traceback (most recent call last):
        ...
    AttributeError: has no attribute empty
    '''
    def __getattr__(self, attr):
        try:
            return self[attr]
        # 这里本来会返回keyError，将其转换成attributeError抛出
        ## 注：dict类型，key值不是其属性
        except KeyError:
            raise AttributeError("has no attribute %s"%attr)
    def __setattr__(self, attr, value):
        self[attr] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
