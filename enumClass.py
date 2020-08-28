from enum import Enum

# 当一个希望一个变量只取有限个数的值时，我们将其定义为一个特定枚举类型的变量
# 首先我们要定义一个枚举类型：用下面方法把Month定义为包含'Jan', 'Feb', 'Mar', 'Apr'四个值的枚举类型
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))
# 当我们需要把mon变量设定为1月时：
mon = Month.Jan
# 可以查看mon实际的值
print(mon.value)
# 这个值一般不需要知道,因为在之后所有对于月份的运算都用Month.xxx来表示，例如：
## 判断mon是不是二月
if mon == Month.Feb:
    print('二月春风似剪刀')
else:
    print('等待二月')


# 枚举类型是可以遍历的
for item in Month:
    print(item, ":", item.value)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

# 我们也可以用如下方法定义一个枚举类，继承Enum就可以。
# unique装饰器可以检查是否有重复的枚举值
@unique
class weekday(Enum):
    Sun = 0
    # Mon = 0     # 和上一个重复会出错
    Mon = 1
    Tue = 2
    Wed = 3
    Thr = 4
    Fri = 5
    Sat = 6
# 用法和上面一样
for day in weekday:
    print(day, ':', day.value)

day1 = weekday.Mon
