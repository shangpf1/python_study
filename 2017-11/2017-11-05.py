'''
我的作业02 继承（子类继承父类）
'''
# 父类
class liming_father():
    def have_money(self):
        print("It is my money")
    def have_car(self):
        print("It is my car")
# 子类
class liming(liming_father): # 子类继承父类
    def eat(self):
        print("I like eat")

li_father=liming_father()
li_father.have_money()
#li_father.have_car()

li=liming()
li.eat()
li.have_car()       # 子类继承父类的方法


class liming_father():
    def have_money(self):
        print("It is my money")
    def have_car(self):
        print("It is my car")
        print("---------------------")

class liming(liming_father): # 子类继承父类
    def eat(self):
        print("I like eat")
    def have_car(self):
        print("这是我的劳斯莱斯")

li_father=liming_father()
li_father.have_money()
li_father.have_car()

li=liming()
li.eat()
li.have_car()       # 子类有自己的方法的话，就执行自己的方法