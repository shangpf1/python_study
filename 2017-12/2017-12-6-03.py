
'''
我的练习作业03 练习实践01

'''

import random
print(random.random())     # 随机生成浮点数

list1=['1','2','3','4','5','6','7','8','9','0']
for y in range(7):                      # 随机生成列表中的7个数
    print(random.choice(list1))



# 随机生成一个手机号码，
# 如：（13xxxxxxxxx,15xxxxxxxxx,17xxxxxxxxx,18xxxxxxxxx）
p=['13','15','17','18']
num=['1','2','3','4','5','6','7','8','9','0']
phonnum=''
for x in range(9):
    phonnum+=random.choice(num)    # 后面的9位是随机生成的
phonnum=random.choice(p)+phonnum    # 前面的2位+后面随机生成的9位，即为手机号
print(phonnum)


#九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print('{}*{}={}\t'.format(y,x,x*y),end='')
    print()




for x in range(1,11):
    print(x,end=' ')
    print(x)


