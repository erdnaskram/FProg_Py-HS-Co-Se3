import time

_m = 3456
_b = 98765
_c = 678

def rand(seed):
    n = seed % _m
    while True:
        # print(n)
        n = (n * _b + _c) % _m
        yield n


_r = rand(int(time.time()))


def randDouble():
    return _r.__next__() / _m


for _ in range(10):
    print(_r.__next__(), "\t", randDouble(), end="\n")

