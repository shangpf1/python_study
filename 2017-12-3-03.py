"""
我的练习作业02-python 元组01

"""

# 元组与字符串类似，下标索引从0开始，可以进行截取、组合等
tup1=('Google','Runoob',1997,2000)
tup2=(1,2,3,4,5)
tup3="a","b","c","d"

print(tup1)
print(tup2)
print(tup3)


# 创建元组
tup4=(50)
print(type(tup4))   # 不加逗号，类型为整型

tup5=(50,)
print(type(tup5))   # 加上逗号，类型为元组


# 访问元组  (访问上面的 tup1 tup2)
print("tup1[0]:",tup1[0])
print("tup2[1:5]:",tup2[1:5])

print(tup1[2])
print(tup2[1:])


# 修改元组 （元组中的元素值是不允许修改的，但可以对元组进行连接组合，如下示：）
tup6=tup2+tup3
print(tup6)


# 删除元组（元组中的元素值是不能删除的，但可用del语句删除这个元组）
tup7=("hello","sunshine","student","study")
print("删除前的元组tup7:",tup7)
del tup7
print("删除后的元组tup7:",tup7)

