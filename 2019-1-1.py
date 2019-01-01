# 获取标题-当前网址-网页源码

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

# 获取标题
print('title',driver.title)

# 打印当前网址
driver.find_element_by_link_text('新闻').click()
print('url',driver.current_url)  

# 获取网页源码
print('source:',driver.page_source)