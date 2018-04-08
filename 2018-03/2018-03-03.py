
# python 项目日期函数优化
# 网址 http://www.runoob.com/python/python-date-time.html

import time
print(time.localtime())

# 获取格式化的时间  最简单的获取可读的时间模式的函数是asctime()
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# 格式化日期

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S")) 
print(time.strftime("%Y-%m-%d_%H_%M_%S"))  #截图可以采用此种方式命名

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y")) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
print('-----------------------------------------------')

# 获取某年某月某日的日期
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历
import calendar

cal = calendar.month(2018,4)
print("以下输出2016年1月份的日历:",cal)