# -*- coding: utf-8 -*-
import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natules = itertools.count(1,step=2)
    getList = []
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    preList = itertools.takewhile(lambda x:x<=2*N-1,natules)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    flag = True
    sumlist = 0
    for n in preList:
        #print(n)
        if flag:
            sumlist+=(4.0/n)
        else :
            sumlist+=(-4.0/n)
        flag=~flag
    # step 4: 求和:
    return sumlist

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')