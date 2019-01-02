# 显式等待和隐式等待

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# ele = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'mnav')))

ele = driver.find_element_by_class_name('mnav')
print(ele.text)

driver.quit()