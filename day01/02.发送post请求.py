'''
发送post请求
 '''
import requests
# 登陆的接口
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone":"18012345678",
#     "pwd":"123456"
# }
# # data传表单参数,content-type:application/x-www-form-urllencoded
# r = requests.post(url,data=user)
# print(r.text)
#
# #
url = "http://www.httpbin.org/post"
user = {
    "mobilephone":"18012345678",
    "pwd":"123456"
}
r = requests.post(url, data=user)
print(r.text)

print("*"*50)
# 用json传参数，Content-Type": "application/x-www-form-urlencoded",
r = requests.post(url, json=user)
# print(r.text)

# 练习：充值接口，给注册的用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobliephone": "18012345678",
    "amount": "3000"
}
r = requests.post(url, data=user)
print(r.text)
assert r.json()["status"] == 1
assert r.json()["code"] =='10001'
assert r.json()["msg"] == '充值成功'
