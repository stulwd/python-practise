# -- test.py --
from myDict import Dict
import unittest

# 继承测试类
## 类中以test开头的方法会被认为是测试方法，在测试时才会执行
class testDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # setUp和tearDown方法分别会在执行每一个测试前后执行
    def setUp(self):
        print("setup...")
    def tearDown(self):
        print("tearDown..")
            
if __name__ == '__main__':
    unittest.main()


# 之后在命令行执行python ./myDict_test.py就会进行全部测试
# 或者运行python -m unittest myDict_test
