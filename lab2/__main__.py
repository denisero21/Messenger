import unittest

from tests.parsers_test import test_parsers
from tests.tests import TestClass
import math


dic = {'lab': 2, 'status': 'done'}
lst = ['first', 'second', 3, {'number': 4}]
tupl = ('test_tuple', {'status': 'ok'}, ('nested_tuple', 'one_more'))


c = 42


def f(x):
    a = 123
    return math.sin(x * a * c)


if __name__ == '__main__':
    test_parsers(dic)
    test_parsers(lst)
    test_parsers(tupl)
    #test_parsers(f)
    TestClass.test_complex_dict(TestClass())

