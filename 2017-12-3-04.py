"""
我的练习作业02-python 元组02

"""

# 元组的索取、截取
L = ('Google','Taobao','Runoob')
print(L)        
print(L[2])     # 读取第三个元素
print(L[-2])    # 反向读取，读取倒数第二个元素
print(L[1:])    # 截取元素，从第二个开始后的所有元素


# 元组内置函数
tuple1 = ('Google','Runoob','Taobao')
print("元组中元素的个数：",len(tuple1))

tuple2 = ('5','4','8')
print("元组中最大的数：",max(tuple2))
print("元组中最小的数：",min(tuple2))

list1 = ['Google','Taobao','Runoob','Baidu']
tuple3 = tuple(list1)         # 将列表转换为元组
print(tuple3)

# tuple函数
list2 = ['hello','world']
print(tuple(list2))

list3 = ('hello','world')
print(tuple(list3))

list4 = 'hello'
print(tuple(list4))
