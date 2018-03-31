import random

# 打印出随机的浮点数
print(random.random())

# 随机产生电话号码的后9位数字
ph = ['18','15','13','17']

num = ['1','2','3','4','5','6','7','8','9','0']
phnum = ''

for x in range(9):
    phnum += random.choice(num)
phnum = random.choice(ph)+phnum
print('随机产生的手机号码：',phnum)


# 打印出1~100之间所有奇数之和
sum =0
for y in range(1,101):
    if y%2!=0:
        # print(y)   打印出所有的奇数
        sum +=y
print('1~100之间所有奇数之和：',sum)


# 打印出1~100之间所有的偶数
h = []
for i in range(1,101):
    if i%2==0:
        h.append(i)
print(h)






    