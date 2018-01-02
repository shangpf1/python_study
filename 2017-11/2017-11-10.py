'''
python 字符串的操作
'''
name = 'liGang'
address = 'china'

# 3种不同的打印方式
print(name,address)
print(name+" "+address)
print('my name is %s,I live in %s'%(name,address))


print("圆周率PI的值：%f"%3.14)     # 默认一般是八位

print("圆周率PI的值：%.2f"%3.14159)   # 小数点后2位

print("圆周率PI的值：%12f"%3.14)      # 字符宽度为12，剩余4个空格

print("圆周率PI的值：%*f"%(10,3.14))     # * 字符宽度为10，剩余2个空格

print(name.capitalize())      # 将字符串中的第一个字符转换为大写    Ligang
print(name.lower())           # 转换字符串中所有大写为小写
print(name.upper())           # 转换字符串中所有小写为大写
print(max(name))              # 返回字符串name中最大的字母
print(min(name))              # 返回字符串name中最小的字母