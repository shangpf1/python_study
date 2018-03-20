import requests


# 主题首页

topic_url = "http://118.31.19.120:3000/api/v1/topics"
topic_data = {
    "page":3,
    "tab":"ask",
    "limit":3,
    "mdrender":"false"
}

re = requests.get(topic_url,topic_data)
print(re.json())


# 创建主题
creat_topic_url = "http://118.31.19.120:3000/api/v1/topics"

edit_topic_url = "http://118.31.19.120:3000/api/v1/topics/update"

userToken = "f4c4a83f-fd31-4f9e-8585-451267cb4288"
creat_data = {
    "accesstoken":userToken,
    "title":"helloworld",
    "tab":"ask",
    "content":"shifdfdgsdhfdsdfdssfsdfdsf"
}

r = requests.post(creat_topic_url,json = creat_data)
print(r.json())

res = r.json()
new_topic_id = res['topic_id']
print("id",new_topic_id)

# 编辑主题
edit_data = {
    "accesstoken":userToken,
    "topic_id":new_topic_id,
    "title":"shdhdfdfff",
    "tab":"ask",
    "content":"sdsfsdfdsfdfdfsdfdfdsfdsfdf"
}

edit_res = requests.post(edit_topic_url,json = edit_data)
print(edit_res.json())

# 收藏主题
coll_topic_url = "http://118.31.19.120:3000/api/v1/topic_collect/collect"

coll_data = {
    "accesstoken":userToken,
    "topic_id":new_topic_id
}

coll_res = requests.post(coll_topic_url,json= coll_data)
print(coll_res.json())

#取消主题
del_topic_url = "http://118.31.19.120:3000/api/v1/topic_collect/de_collect"
del_data = {
   "accesstoken":userToken,
    "topic_id":new_topic_id 
}

del_res = requests.post(del_topic_url,json= del_data)
print(del_res.json())

#用户所收藏的主题
loginname_coll_topic_url = "http://118.31.19.120:3000/api/v1/topic_collect/testuser01"

login_res = requests.get(loginname_coll_topic_url)
print(login_res.json())



