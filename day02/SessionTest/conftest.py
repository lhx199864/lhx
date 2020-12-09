'''
fixture作用域：session级别
公共方法放到conftest.py文件中，文件名不能写错，pytest是根据文件名找到对应的方法
1.conftest 文件可以存在多个
2.conftest在SessionTest目录下，对SessionTest下的py文件及子目录下的py文件生效
3.conftest放到ApiAutotest目录下，对整个工程生效
4.不用import

'''
import pytest

# session 级别的，整个执行过程，开始前执行前置，所有执行完了以后执行后置
@pytest.fixture(scope='session')
def login():
    print("登录系统")
    yield
    print("退出系统")