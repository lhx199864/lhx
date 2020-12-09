'''
测试前置和后置
测试前置;测试环境的初始化测试脚本的执行前的准备
测试后置：环境的清理

'''
# 模块与函数级配合使用
# 模块机：前置在模块开始执行一次，后置在模块结束后执行一次
# 函数级前置在每个函数开始执行一次后置在每一个函数结束执行后执行一次

def setup_module():
    print("测试前置:module级别的")
def teardown_module():
    print("测试后置:module级别的")

def setup_function():# 名字不能写错
    print("测试前置:function级别的")
def teardown_function():
    print("测试后置:function级别的")
def teardown_function():
    print("测试后置:function级别的")

def test_001():
    print("测试脚本1")
def test_002():
    print("测试脚本2")
def test_003():
    print("测试脚本3")