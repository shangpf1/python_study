"""
我的练习作业03 python 元组tuple、列表list、字典dict

"""

# 元组

tuple=('a','b','c','d','e','f')
for x in tuple:        #迭代
    print(x)

print(len(tuple))      # 长度

list1= list(tuple)     # 元素转为列表
print(list1)           # 将列表打印出来

print('a' in list1)    # 元素是否在列表中

for x in list1:        # 迭代
    print(x)

print(max(tuple))       # 元组中最大值
print(min(tuple))       # 元组中最小值


# 列表

list2 = [1,1,84,25,252,"23d",'fsdafa']
s = set(list2)                          # set 过滤取重复的  结果： 打印结果顺序随机变化
lista=list(s)          
print(lista)                            # 打印结果随机排序的


# 字典（无序的对象集合，不存在切分）

dir1={0:'BigWo',1:'xjx',2:'cwj',3:'xyz',4:'dxl',5:'sy',
        6:'spf',7:'yll',8:'gyh',9:'yh',
        10:'zwq',11:'wjc',12:'zxj',13:'zy'}
print(dir1)

dict2={(1,2,3,4,5):90,6:80,7:70,8:60}
dict2[(1,2,3,4,5)]=100          # 将字典中的前5个键对的值更新为100
print(dict2)

dict2[9]=110         # 在字典新增一个键对的值
print(dict2)        

dir1[15]='pfx'
print(dir1)

del dict2[9]          # 删除字典中第9个键值对的值
print(dict2)

print(dict2[6])       # 取第6个键对的值打印

dict2.clear()     # 清空整个字典dict2
print(dict2)


del dict2()     # 删除整个字典
print(dict2)



