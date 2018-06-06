# 安居客 https://login.anjuke.com/login/form    定位需要 iframe


from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://login.anjuke.com/login/form')

driver.switch_to_frame('iframeLoginIfm')

driver.find_element_by_id('phoneIpt').send_keys('18791042625')
driver.find_element_by_id('smsIpt').send_keys('34354645566')