# 通过switch_to_windows可以操作多个窗口

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.baidu.com")

# 输入helloworld后点击按钮
driver.find_element_by_id('kw').send_keys('helloworld')
driver.find_element_by_id('kw').submit()

# 点击搜索结果中的任一项
driver.find_element_by_xpath('//*[@id="3"]/h3/a').click()

# 打印所有窗口的长度
wds = driver.window_handles
print('all windows:',len(wds))

# 打开第2个窗口
driver.switch_to_window(wds[1])

# 标题并打印标题
h1 = driver.find_element_by_css_selector('#article > div.article-title > h2')
print('h1:',h1.text)


执行结果：

DevTools listening on ws://127.0.0.1:57864/devtools/browser/4e5cc38d-8772-4700-a24b-b34b3091c2d5
all windows: 2
h1: 跟我学java编程—用eclipse创建第一个HelloWorld项目