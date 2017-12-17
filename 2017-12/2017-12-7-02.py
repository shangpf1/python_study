'''
斐波那契数列 

'''

# def test(a):
#     a+=1
#     print(a)
# test(10)

num = int(input("请输入你要的次数:"))
n1=0
n2=1
nth=0
counter=0
list=[n1,n2]
while counter<num:
    nth=n1+n2
    n1=n2
    n2=nth
    counter+=1
    list.append(nth)
print(list)

# 方法1：通过值来控制（输入的范围内）

x=int(input('请输入数字的范围：'))
def test1():
    n1,n2=0,1
    list=[n1,n2]
    nth=0
    for i in range(0,x):
        nth = n1 +n2
        if nth <= x:
            n1 = n2
            n2 = nth
            list.append(nth)
        print(nth)
    print (list)
test1()          

# 方法2：通过值来控制（输入的范围内）

x = int(input('enter a number:'))
n1,n2=0,1
list = [n1,n2]
nth=0         # 后面的值

while True:
    # n3:1  = n2+ n3  0 1
    nth = n1 + n2
    if nth > x:      # 后面的值大于前面的值，会跳出   输入的x值，nth大于x的话就会跳出(后面的nth等于前面2个数的和)
        break
    #  n1 =1
    n1 = n2         # 会将前面的值替换掉
    # n2 = 1
    n2 = nth
    list.append(nth)   
    #print(nth)
print (list)

