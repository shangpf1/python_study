"""
判断从键盘输入的成绩，大于90优秀，60-90及格，0-60不及格，其他输入“不合法分数输入”

"""

score= input("输入成绩:")
score=int(score)
if score>90 and score<=100:
    print("优秀")
elif score>60 and score<=90:
    print("及格")
elif score>0 and score<=60:
    print("不及格")
else:
    print("不合法的输入")