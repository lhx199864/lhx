'''
fixture带参数

'''


import pytest
import requests

@pytest.fixture(params=[{"username": "root", "pwd": "123456"},
                        {"username": "admin", "pwd": "888888"},
                        {"username": "administrator", "pwd": "HelloPwd"},
                        "four",
                        5])
def login_data(request):  # 参数request 是固定的，不能写成其他的
    return request.param  # 使用request.param返回每组数据


# 测试逻辑
# 登陆功能的测试脚本
def test_login(login_data):
    print(f"测试登陆功能，测试数据为:{login_data}")


  # 练习:注册接口的测试代码 用这种方式来实现
@pytest.fixture(params=[{"data": {"mobilephone": "19012345678", "pwd": "123456"},
                         "expect": {"msg":"注册成功", "code": "10001"}},
                        {"data": {"mobilephone": "18012345678", "pwd": "12"},
                         "expect": {"msg": "密码长度为6~18位", "code": "20108"}},
                        ])
def register_data(request):
    return request.param

def test_register(register_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    print("测试数据",register_data['data'])
    print("测试结果", register_data['expect'])
    r = requests.post(url, data=register_data['data'])
    print(r.text)
    assert r.json()['msg'] == register_data['expect']['msg']
    assert r.json()['code'] == register_data['expect']['code']