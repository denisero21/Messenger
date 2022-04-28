from tests.test_parsers import test_parsers
import math
from serializer.serializer import serialize_function, deserialize_function

c = 42
def f(x):
    a = 123
    return math.sin(a*x*c)

def m(a, b):
    return a + b

def test_fact(n):
    if n == 0:
        return 1
    else:
        return n * test_fact(n - 1)


dct = {'fa': 3, 'a': '4', 5: 6.923}
lst = ['first', 'second', 3, {'number': 4}, dct]
tupl = ('test_tuple', True, {'status': 'ok'}, ('nested_tuple', 'one_more'), lst)

if __name__ == '__main__':
    test_parsers(dct)
    test_parsers(lst)
    test_parsers(tupl)
    res = test_parsers(m, True, 'json')
    print(res(10, 5))
    res = test_parsers(test_fact, True, 'toml')
    print(res(10))
    #res = test_parsers(f, True, 'json')
    print(res(99))
    print()
