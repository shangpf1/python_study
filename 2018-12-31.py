# 浏览器最大化窗口、截屏

from selenium import webdriver
from os import path


driver = webdriver.Chrome()

d = path.dirname('__file__')
index = path.join(d,'index.png')

driver.get("https://www.baidu.com/")

# 最大化窗口
driver.maximize_window()

# 截屏
driver.save_screenshot(index)

# 后退操作
driver.back()

# 前进操作
driver.forward()

# 刷新操作
driver.refresh()

driver.quit()