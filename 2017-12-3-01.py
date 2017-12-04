"""
我的练习作业02-python列表

"""

list 1=[1,2,3,4,5]

list2=["td","fgh"]

list3=[[1,2,3],[4,5,6]]

print(max(list3))
print(min(list3))

list4 = ["Google","Runoob",1997,2000]
list5 = [1,2,3,4,5,6,7]

# 切片
print("list4[1]:",list4[1])
print("list5[1:5]:",list5[1:5])
print("list5[1:5:2]:",list5[1:5:2])
print(list5[1:])
print(list5[:-1])
print(list5[:])

# 更新列表
print("第三个元素是：",list4[2])

list4[2]=2080
print("最后更新的第三个元素是：",list4[2])


# 删除列表元素
print(list4)
del list4[1]
print("删除列表后的元素：",list4)

print(len([1,2,3,4]))       # 长度

list5=[1,2,3]+[4,5,6]       # 组合
print(list5)

list6=['HI!'*5]             # 重复
print(list6)

list7=4 in[6,7,3,4]         # 元素是否存在列表中
print(list7)

