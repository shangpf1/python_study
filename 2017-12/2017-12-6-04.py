'''
我的练习作业03 

'''

# n=100
# counter=1
# sum=0
# while counter<=n:
#     sum+=counter
#     counter+=1
# print(sum)





# list = [1,2,3,4]
# b=iter(list)
# print(next(b))
# next(b)
# next(b)

# for x in b:
#     print("b==",x)


# a=1
# while a<10:
#     print(a)
#     a+=1


list1=[11,24,36,48,56,60,71,83]
for i in range(len(list1)):
    for j in range(i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
    print(list1)




# listy=[2,42,6,83,21,6,7,32,4,5,7,6,34,3]
# for i in range(len(listy)):
#     for j in range(i):     # 在第一次的基础上进行
#         if listy[j]>listy[j+1]:
#             listy[j],listy[j+1]=listy[j+1],listy[j]
#     print(listy)



# a=1
# while a<=10:
#     print(a) 
#     a+=1

# for x in range(1,11):
#     print(x)



list3=[45,65,76,876,90]
list4=[1,2,4,5,67]
list3.extend(list4)

list3[5]=100
list3.append(6)

print(list3)



