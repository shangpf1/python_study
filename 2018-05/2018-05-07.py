from selenium  import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 获取输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text1 = driver.find_element_by_id('lh').text
print(text1)
text = driver.find_element_by_id('cp').text
print(text)

# 返回元素的属性值，可以是 id name class type 或其他任何属性
attribute = driver.find_element_by_id('kw').get_attribute('class')
print(attribute)

# 返回元素的结果是否可见，返回结果为 True 或 False
result = driver.find_element_by_id('kw').is_displayed()
print(result)


# 返回结果如下示：
# {'height': 22, 'width': 500}
# 把百度设为主页关于百度About  Baidu百度推广
# ©2018 Baidu 使用百度前必读 意见反馈 京ICP证030173号  京公网安备11000002000001号
# s_ipt
# True
