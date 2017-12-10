"""
我的练习作业03- python  list列表复习

"""

list1=[1,2,324,36,88,'sfgh','dfe','pkefg']
list2=['a','b','c']

list1[1:5]=1,1,1,1       # 将列表中前面的数字都更新为1
list1[5:8]='a','a' ,'a'    # 将列表中后面的字符都更新为a
print(list1)

list1[0]=list2      # 将list2嵌套到list1[0]位置
print(list1)

for x in list1:
    #print(x)
    print(x,end=" ")

str='sdfdg'
s= list(str)
print(s)            #以列表的形式打印
print(type(s))      #字符串的类型

list1.extend(list2)    #将list2打撒放进去   结果：[1, 2, 324, 36, 88, 'sfgh', 'dfe', 'pkefg', 'a', 'b', 'c']
list1.append(list2)     #将list2整个整体放进去  结果：[1, 2, 324, 36, 88, 'sfgh', 'dfe', 'pkefg', ['a', 'b', 'c']]

list1.pop()            # 按最后的开始删除   结果：[1, 2, 324, 36, 88, 'sfgh', 'dfe']
list1.reverse()        # 倒序  结果：['dfe', 'sfgh', 88, 36, 324, 2, 1]
print(list1)


list3=list2.copy()      # 将list2复制后复制给list3
list3.clear()           # 将list3清空
print(list3)

