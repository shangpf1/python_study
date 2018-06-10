from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# 打开CNode 社区网站
driver.get('http://118.31.19.120:3000/signin')

# 输入用户名、密码
driver.find_element_by_id('name').send_keys('testuser8')
driver.find_element_by_id('pass').send_keys('123456')

# 点击登录
driver.find_element_by_class_name('span-primary').click()

# 点击发布话题
driver.find_element_by_class_name('span-success').click()

driver.find_element_by_css_selector('#tab-value > option:nth-child(2)').click()

driver.find_element_by_id('title').send_keys('2018-06-07')

# driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre').send_keys('today is sunday')

# 光标定位
contentInput = driver.find_element_by_class_name('CodeMirror-scroll')
ActionChains(driver).move_to_element(contentInput).click().perform()

driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre').click()
ActionChains(driver).move_to_element(contentInput).send_keys('原来如此，还是需要加强练习，加油！加油！加油！-----sunshine').perform()

#提交按钮
driver.find_element_by_class_name('submit_btn').click()

