"""

我的练习02-python 位运算符

"""

a = 60      # 60 = 0011 1100 
b = 13      # 13 = 0000 1101
c = 0

c = a & b   # c = 0000 1100  位与运算符，两个相对应位为1，则为1，否则为0
print ("line 1 - c 的值为：",c)

c = a | b   # 61 = 0011 1101  位或运算符，和位与运算相反，两个钟有1个位1，则为1
print ("line 2 - c 的值为：",c)

c = a ^ b   # 49 = 0011 0001  位异或运算符，
print ("line 3 - c 的值为：",c)

c = ~ a     # -61 = 1100 0011  位取反运算符
print ("line 4 - c 的值为：", c)

c = a << 2  # 240 = 1111 0000   左移动运算符
print ("line 5 - c 的值为：",c)

c = a >> 2    # 15 = 0000 1111   右移动运算符
print ("line 6 - c 的值为：",c)






