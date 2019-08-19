import time
import functools

def metric(fn):
    start = time.time()
    def excuteFn(*args,**kwargs):
        return fn(*args,**kwargs)
    end = time.time()
    print("%s executed in %s ms "%(fn.__name__,(end-start)))
    return excuteFn

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print("f:%s"%f)
print("s:%s"%s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')