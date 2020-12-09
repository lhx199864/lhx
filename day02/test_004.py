'''
fixture 测试前置后后置  比较常用的方式
1.命名比较灵活，不限于setup,teardown等命名格式
2.使用比较灵活
3.不需要import计科实现共享

'''

import pytest

# 测试前置
@pytest.fixture()
def login():
    print("登陆系统")  # yield之前是前置
    yield
    print("退出系统")  # yield之后是后置

# 测试脚本
def test_query():
    print("查询功能，不需要登录")

# 使用方式一：将fixture作为参数传到脚本中
def test_add(login):
    print("添加功能，需要登录")

# 使用方式二;使用装饰器userfixyures
@pytest.mark.usefixtures("login")
def test_delete():
    print("删除功能，需要登录")