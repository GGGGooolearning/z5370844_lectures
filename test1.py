# import numpy
# from package import something()

class Student:
    # stuCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Student.stuCount 访问
    stuCount = 0

    def __init__(self, name, sid):
        self.name = name
        self.sid = sid
        Student.stuCount += 1

    def displayCount(self):
        print('Total Student %d' % Student.stuCount)
        # print(type(Student.stuCount))

    def displayStudent(self):
        print("Name : ", self.name, '\n', "Student ID : ", self.sid, '\n')
        # print('{} {}'.format(self.name, self.sid))
        # print(f'sdfsfdsf {variable} dfsfdsf')


class Test:
    def prt(self):
        print(self)
        # print(type(self))
        # self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类
        print(self.__class__)


# student类的实例对象std
std1 = Student(1, '001')
std2 = Student(2, '002')
std1.displayCount()
std1.displayStudent()
std2.displayCount()
std2.displayStudent()

# 添加修改类的属性
std1.age = 20  # 添加属性
print(getattr(std1, 'age'))
print(hasattr(std1, 'age'))
print(hasattr(std2, 'age'))
del std1.age
print(hasattr(std1, 'age'))

# getattr(obj, name[, default]) : 访问对象的属性。
# hasattr(obj,name) : 检查是否存在一个属性。
# setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
# delattr(obj, name) : 删除属性

# pt = Test()
# pt.prt()

# 内置类属性
# __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

print("Student.__doc__:", Student.__doc__)
print("Student.__name__:", Student.__name__)
print("Student.__module__:", Student.__module__)
print("Student.__bases__:", Student.__bases__)
print("Student.__dict__:", Student.__dict__)

# 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行

list = ['apple', 'jack', 798, 2.22, 36]
otherlist = [123, 'xiaohong']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 输出列表第二个至第三个元素
print(list[2:])  # 输出列表第三个开始至末尾的所有元素
print(otherlist * 2)  # 输出列表两次
print(list + otherlist)  # 输出拼接列表

dict = {}
dict['one'] = 'This is one'  # key是one，value是This is one
dict[2] = 'This is two'
tinydict = {'name': 'john', 'code': 5762, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one'的值
print(dict[2])  # 输出键为2的值
print(dict)
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('Ru\noob')
print(r'Ru\noob')

# if __name__ == "__main__":
# if __name__ == '__main__' 就相当于是Python 模拟的程序入口。 Python
# 本身并没有规定这么写，这只是一种编码习惯。 由于模块之间相互引用，
# 不同模块可能都有这样的定义，而入口程序只能有一个。 到底哪个入口程序被选中，这取决于 __name__ 的值。


