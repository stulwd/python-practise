# 字符串不转义：字符串前加r
str = r"\task"

# 字符编码：计算机内存中统一使用unicode编码，储存或传输时使用utf-8
## 关于文件编码：我们看到的屏幕上的东西都是unicode格式的，而存在硬盘上的东西是经过编码后的格式。
## 所以即使file1是utf-8，file2是utf-16格式，当他们打开后，都经过了相应的解码器，变成统一的unicode格式。
## 所以在都打开的情况下，两个文件可以自由相互复制内容，保存时会编码成他们自己的格式储存。

# 内存中的'中'是unicode编码，其十六进制是0x4e2d
hex(ord('中'))
# 将其编码为utf-8格式时，是3个字节b'\xe4\xb8\xad'
'中'.encode('utf-8')
'\u4e2d'.encode('utf-8') 
# 下面代码语句将会被存储为 b'printf("\xe5\x8f\x91\xe9\x92\xb1")'
'print("发钱")'.encode('utf-8')

## 查看字符对应的编码
c = ord('d') 
## 查看编码对应的字符
chr()

# 数字的进制表示法
## 二进制
0b0110
## 八进制表示
0o0707
## 十进制表示
1234
## 十六进制表示
0x23

# 进制转换
## 转换为二进制
bin()
## 转换为八进制
oct()
## 转换为十进制
ord()
## 转换为十六进制
hex()


# list方法:insert append pop
l = [1,2,3,4]
l.insert(4, 5)
l.append(6)
l.pop() # 弹出6
l.pop(1) # 弹出索引元素

# tuple：一级元素不能修改

# input用法
num = int(input("请输入一个整数："))

# dict：get方法、pop方法
d = {'a':1, 'b':2, 'c':3}
d.get('d', '不存在')
d.pop('c')
d.copy()

# set: add方法和remove方法
s = {1,2,3,4}
s.add(1) # 添加失败
s.add(5) # 添加成功
s.remove(1) # 成功
s.remove(1) # 成功

# 切片
l[-2:] # 取后

