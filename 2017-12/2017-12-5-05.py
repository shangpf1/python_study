"""
我的练习作业03 python 字典dict 练习02

"""

student={'name':'shangf','age':23,'sex':'男','id':24555,'phone':276666777}
print(student)

# list1=list(student.items())    # 以列表返回可遍历的（键,值）元组数组
# print(list1)

student['class']="1302班"
print(student)

a=student.get('age')
print(a)                               # 打印出年龄

if a>=22:
    student['job']="测试工程师"
    print(student.get('job'))
elif a<22:
    student['job']="学生"
    print(student.get('job'))

j=student.get('job')
if j=="测试工程师":
    student['salary']="10K"
    print(student.get('salary'))
elif j=="学生":
    student['salary']="0K"
    print(student.get('salary'))
else:
    print("has no job !!!")