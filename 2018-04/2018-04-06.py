# 参考视频 2018-01-31 类的构造方法和私有属性

class Person:
    # 构造函数
    def __init__(self,username,passwd,email):
        self.username = username
        self.__passwd = passwd   # 私有属性，好处：在外部无法修改，只能在内部修改
        self.email = email

    def get_passwd(self):
        return self.__passwd

    # 如果在外部修改需要此函数
    def set_passwd(self,val):
        self.__passwd = val

    def register(self):
        print('user_register',self.username,self.__passwd,self.email)

    def login(self):
        print('user_login',self.username,self.__passwd)

p = Person('xiaofei','123456','123456@123.com')
p.login()
# p.__passwd ='243454556565657'
p.set_passwd('455465767687989')
p.login()

# p2 = Person('xiaozheng','12345','234345@126.com')
# p2.register()