# 先进行alert文件的脚本编写(如下示：)，在浏览器中打开复制其路径即是下方的路径   需要用到alert库

# <button onclick="altermsg()">click me </button>
# <script>
#     function altermsg(){
#         alert('hello world')
#     }
# </script>

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()


driver.get('file:///D:/Learn-python/python_study/2018-05/alert.html')
driver.find_element_by_tag_name('button').click()

Alert(driver).accept()