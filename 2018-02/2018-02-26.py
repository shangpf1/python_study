
import requests

# # 1. python接口自动化-requests库模拟用户登录

# url = "https://api.github.com/user"

# r = requests.get(url,auth=('shangpf1','spf123456'))
# print(r.json())


#  2. python接口自动化-requests发送post请求

import json

url = "https://api.github.com/user/repos"

post_data = {
	"name":"helloworld"
}
r = requests.post(url,json=post_data,auth=('shangpf1','spf123456'))
print(r)

