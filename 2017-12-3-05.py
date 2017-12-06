"""
我的练习作业02-python 字符串01

"""

# python访问字符串中的值
var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]:",var1[0])
print("var2[1:5]:",var2[1:5])


# python字符串更新
var3 = 'Hello World!'
print("更新后的字符串：",var3[:6]+'Runoob!')


# python字符串运算符
a = "Hello"
b = "Python"

print("a+b 输出结果：",a+b)
print("a*2 输出结果：",a*2)
print("a[1] 输出结果：",a[1])
print("a[1:4] 输出结果：",a[1:4])

if("H" in a):
    print("H 在变量 a 中")

else:
    print("H 不在变量 a 中")

if("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

