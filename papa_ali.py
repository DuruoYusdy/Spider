#爬虫测试版
#需要安装selenium,phantomJS
#第一步：用selenium模拟手动操作浏览器提交表单，不能用requests，因为每次登陆请求的url是生成的，非固定
#第二步：登陆进去后，记录下cookie,模拟ajax请求数据，存到临时文件temp.json

import requests
from selenium import webdriver

url = "https://eco.alibaba.com/login.htm"    #登陆界面
dourl = "https://eco.alibaba.com/###.ajax"  #模拟ajax请求
data = {
    '_tb_token_': '#',
    'action': '#',
    'appId': '#',
    'endDate': 'begintime',
    'startDate': 'endtime',
    'systemType': 'log'
}

driver = webdriver.Chrome()

r = requests.get(url)
print(r.text)

#登陆处理
driver.get(url)

name = driver.find_element_by_xpath('//*[@id="fm-login-id"]')
password = driver.find_element_by_xpath('//*[@id="fm-login-password"]')
name.send_keys("username")       #把此处更改为真实姓名
password.send_keys("password")   #把此处更改为真实密码
driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()

#转化cookie值
cookies = driver.get_cookies()
s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'],cookie['value'])

#请求ajax
r = s.post(dourl,data=data)
print(r.text)
f = open('./temp.json', 'w')
f.write(r.text)
driver.quit()
