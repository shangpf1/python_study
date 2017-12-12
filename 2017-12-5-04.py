"""
我的练习作业03 python 字典dict 练习01

"""

dir1={0:'fdgfdh',1:'ffhjj',2:'ytuy',3:'dfdfg'}
s= str(dir1)
print(type(s),type(dir1))
print(s)
print(dir1)

t=dir1.values()   # 以列表返回字典中的所有的值（过滤掉键位）
list1=list(t)
print(list1)

keys= dir1.keys()    # 以列表返回一个字典所有的值（过滤掉键值）  相当于：list2=list(dirl)将其打印
list2=list(keys)
print(list2)

items=dir1.items()     # 以列表返回可遍历的（键,值）元组数组
list3=list(items)
print(list3)

print('fshsg' in dir1)
print('ytuy'in dir1)


dir1.pop(0)           # 删除 dir1 中第1个键值对
dir1.popitem()         # 删除 dir1 中最后1个键值对
print(dir1)

print(dir1.get(1))       # 等于取下标 dir1[1]的值（dir1中第2个键值对的值）

