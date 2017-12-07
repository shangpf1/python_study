"""
我的练习作业02-python 字符串02

"""

# python 字符串格式化
print("我叫 %s ，今年 %d 岁！" % ('小明',10))  # %s 格式化字符串  %d 格式化整数

print("圆周率PI的值为：%f"%3.14)               # %f 格式化浮点数字，可指定小数点后的精度

print("圆周率PI的值为：%.2f" %3.14)            # 保留小数点后2位

print("圆周率PI的值为：%10f" %(3.14))          # 字符宽度为10，剩余2个空格

print("圆周率PI的值为：%12f" %(3.14))          # 字符宽度为11，剩余3个空格

print("圆周率PI的值为：%*f"%(10,3.14))


# python三引导

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)



# python 的字符串内建函数
str="  nffDFGhg"
print(str.capitalize())         # capitalize() 将字符串的第一个字符转换为大写

print(str.lower())              # 转换字符串中的大写字母为小写

print(str.lstrip())             # 截取字符串左边的空格或指定字符 

print(max(str))                 # 返回字符串str中最大的字母
print(min(str))                 # 返回字符串str中最小的字母

print(str.upper())              # 转换字符串中的小写字母为大写 
 




