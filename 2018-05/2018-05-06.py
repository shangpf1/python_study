from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
driver.maximize_window()


# submit() 模拟输入关键字后的 “回车” 操作
search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()

# driver.close()
driver.quit()


