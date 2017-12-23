'''
我的练习作业02-python 定义一个函数（define a function by yourself）

'''

def ChangeInt(a):
    a = 3
b = 2
ChangeInt(b)
print(b)


def add(a):
    print(a,3+4)
add("3")

# 用2中方法打印3条边是否组成三角形
def sanjx(a,b,c):
     if a+b>c and a+c>b and b+c>a:
         print("ok")
     else:
         print("no")
sanjx(2,3,4)


def sanjx():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    if a+b>c and a+c>b and b+c>a:      # IndentationError: unexpected indent 提示前面有空格，没对齐
         print("ok")             
    else:
         print("no")
sanjx()


def flag(a,h):
    s=(a*h)/2
    return s
print(flag(3,7))


def num():
    score1=int(input("输入分数1："))
    score2=int(input("输入分数2："))


    if (score1>90 and score2>=70) or (score1>=80 and score2>=80):
        print("很好，给你独孤九剑剑谱。")
    else:
        print("不孝徒儿，去思过崖闭门思过去吧！")
num()


def  num_2(a):
    a=3+2
    return a

print(num_2(9))      # 打印出来还是上面取得a值







