'''
我的练习作业02  创建类，将类进行实例化 
'''

# 创建一个动物类，它可以能吃能喝能睡
class animal:
    def __init__(self):
        print("创建函数时要调用构造函数")
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")
    def sleep(self):
        print("sleep")

elephant = animal()
elephant.eat()
elephant.drink()
elephant.sleep()


# 创建一个人类，他可以能吃能喝能爱
class human:
    def __init__(self,name):
        print("创建函数时要调用构造函数")
    def eat(self,name):
        print(name,"can eat")
    def drink(self,name):
        print(name,"can drink")
    def love(self,name):
        print(name,"can love")

name = human("john")
name.eat("john")
name.drink("john")
name.love("john")