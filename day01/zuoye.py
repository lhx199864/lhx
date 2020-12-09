
import requests
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18012345672",
#     "pwd": "123456"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 1   # 对结果进行检查
# assert r.json()['code'] == '10001'
# assert r.json()['msg'] == '注册成功'

# user = {
#     "mobilephone": "18012345673",
#     "pwd": "123456123456123456"
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 1   # 对结果进行检查
# assert r.json()['code'] == '10001'
# assert r.json()['msg'] == '注册成功'

# user = {
#     "mobilephone": "18012345674",
#     "pwd": "123456",
#     "regname": "Hello"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 1
# assert r.json()['code'] == '10001'
# assert r.json()['msg'] == '注册成功'

# user = {
#     "mobilephone": "18012345675",
#     "pwd": "123456123456123456",
#     "regname": "Hello"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 1
# assert r.json()['code'] == '10001'
# assert r.json()['msg'] == '注册成功'
# 5
# user = {
#     "pwd": "123456"
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20103'
# assert r.json()['msg'] == '手机号不能为空'
# 6
# user = {

#     "pwd": "123456",
#     "regname": "Hello"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20103'
# assert r.json()['msg'] == '手机号不能为空'
# 7
# user = {
#     "mobilephone": "123456",
#     "pwd": "123456",
#     "regname": "Hello"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# # 8
# user = {
#     "mobilephone": "123456",
#     "pwd": "123456",
#     "regname": "Hello"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 9
# user = {
#     "mobilephone": "1234567891011",
#     "pwd": "123456",
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 10
# user = {
#     "mobilephone": "1234567891011",
#     "pwd": "123456",
#     "regname": "Hello"


# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 11
# user = {
#     "mobilephone": "#@$%123456",
#     "pwd": "123456",
#
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 12
# user = {
#     "mobilephone": "#@$%123456",
#     "pwd": "123456",
#      "regname": "Hello"
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 13
# user = {
#     "mobilephone": "开开开123456",
#     "pwd": "123456",
#
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 14
# user = {
#     "mobilephone": "开开开123456",
#     "pwd": "123456",
#     "regname": "Hello"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 15
# user = {
#     "mobilephone": "23312345678",
#     "pwd": "123456",
#      "regname": "Hello"
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# # 16
# user = {
#     "mobilephone": "23312345678",
#     "pwd": "123456",
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20109'
# assert r.json()['msg'] == '手机号码格式不正确'
# 17
# user = {
#     "mobilephone": "18012345678",
#     "pwd": "12345",
#      "regname": "Hello"
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20108'
# assert r.json()['msg'] == '密码长度为6~18'
# 18
# user = {
#     "mobilephone": "18012345678",
#     "pwd": "12345",
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20108'
# assert r.json()['msg'] == '密码长度为6~18'
# 19
# user = {
#     "mobilephone": "18012345678",
#     "pwd": "1234561234561234561234567",
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20108'
# assert r.json()['msg'] == '密码长度为6~18'
# 20
# user = {
#     "mobilephone": "18012345678",
#     "pwd": "1234561234561234561234567",
#     "regname": "Hello"
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20108'
# assert r.json()['msg'] == '密码长度为6~18'
# # 21
# user = {
#     "mobilephone": "18012345678",
#     "regname": "Hello"
#
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20103'
# assert r.json()['msg'] == '参数不能为空'
# 22
# user = {
#     "mobilephone": "18012345678",
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20103'
# assert r.json()['msg'] == '参数不能为空'
# 23
# user = {
#     "mobilephone": "18012345678",
#     "pwd": "123456"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20110'
# assert r.json()['msg'] == '手机号已被注册'
# 24
# user = {
#     "mobilephone": "18012345678",
#     "pwd": "123456",
#     "regname": "Hello"
#
# }
# r = requests.post(url, data=user)
# print(r.json())
# assert r.json()['status'] == 0
# assert r.json()['code'] == '20110'
# assert r.json()['msg'] == '手机号已被注册'
# 登陆
user = {
    "mobilephone": "18012345678",
    "pwd": "123456",

}
r = requests.post(url, data=user)
print(r.json())
assert r.json()['status'] == 1
assert r.json()['code'] == '10001'
assert r.json()['msg'] == '登录成功'





