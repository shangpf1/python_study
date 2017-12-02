"""
我的练习作业02-pytho 逻辑运算符

"""

a = 10
b = 20

if ( a and b ):
    print ("line 1 - 变量 a 和  b 都为 true")
else:
    print ("line 1 - 变量 a 和 b 有一个不为true")

if ( a or b ):
    print ("line 2 - 变量 a 和 b 都为true,或其中一个变量为true ")
else:
    print ("line 2  - 变量 a 和 b 都不为true")

#  修改变量 a 的值
a = 0
if ( a and b ):
   print ("line 3 - 变量 a 和 b 都为true")
else:
    print ("line 3 - 变量 a 和 b 有一个不为true")

if ( a or b ):
   print ("line 4 - 变量 a 和 b 都为true,或其中一个变量为true")
else:
    print ("line 4 - 变量 a 和 b 都不为true")

if not( a and b ):
    print ("line 5 - 变量a 和 b 都为false，或其中一个变量为true")
else:
    print ("line 5 - 变量 a 和 b 都为true")