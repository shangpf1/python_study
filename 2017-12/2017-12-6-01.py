'''
我的练习作业03 python-homework01

'''

# 求从10到100中能被3或5整除的数的和
sum=0
for x in range(10,101):
   if(x%3==0 or x%5==0):
       sum+=x
print(x,sum)



# #求从1~100的奇数和 (2种方法如下：)
sum=0
i=1
while i<101:
    sum+=i
    i+=2
print("1~100的奇数和：",sum)


sum=0
for x in range(1,101,2):
    sum+=x
print(x,sum)


# # 求从1~10的所有偶数
for y in range(1,11):
    if(y%2==0):
        print(y)
print('=======================')
