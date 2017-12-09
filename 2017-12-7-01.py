"""
我的练习作业03  python3 字典

"""

# 创建字典
dict1 = {'abc':456}
dict2 = {'abc':123,98.6:37}
print(dict1)
print(dict2)

dict = {'Name':'Runoob','Age':7,'Class':'First'}

print("dict['Name']:",dict['Name'])
print("dict['Age']:",dict['Age'])


# 修改字典（向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对）
dict = {'Name':'Runoob','Age':7,'Class':'First'}
dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"     # 添加信息

print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])


# 删除字典元素
del dict['Name']     # 删除键 'Name'
dict.clear()         # 删除字典
del dict             # 删除字典

print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])


# 字典键的特性
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次后，最后的值会被记住
dict = {'Name':'Runoob','Age':7,'Class':'First'}
dict = {'Name':'Runoob','Age':7,'Name':'小菜鸟'}     
print("dict['Name']:",dict['Name'])

# 2)键必须不可变，所以可以用数字、字符串或原则充当，但是用列表就不行
 dict = {['Name']:'Runoob','Age':7}
 print("dict['Name']:",dict['Name'])


