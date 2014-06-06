from __future__ import print_function


def step100():
    print('test 1')


scenario = [
    (100, step100),
    (200, lambda: print('test 2')),
    (300, lambda: print('test 3')),
    (400, lambda: print('test 4')),
]