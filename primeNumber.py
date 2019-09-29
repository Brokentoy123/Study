def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_disvisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_disvisible(n), it)  # 构造新序列


if __name__ == "__main__":
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
