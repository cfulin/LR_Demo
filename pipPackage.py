from __future__ import division


def calc_prod(lst):
    def c_prod():
        return reduce(lambda x, y: x*y, lst)
    return c_prod

f = calc_prod([1, 2, 3, 4])
print f()


print sorted([1, 3, 9, 5, 0], lambda x, y: -cmp(x, y))


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

import functools

sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: -cmp(s1, s2))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

import logging


print logging.log(10, 'something')

from os.path import isdir, isfile

print isdir(r'C:/Users/Administrator/Desktop/Python')
print isfile(r'C:/Users/Administrator/Desktop/Python/Data Structures and Algorithms Using Python.pdf')
print 10/3
print 10/3

