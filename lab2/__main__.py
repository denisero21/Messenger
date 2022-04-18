from parsers_test import test_parsers

dic = {'lab': 2, 'status': 'done'}
lst = ['first', 'second', 3, {'number': 4}]
tupl = ('test_tuple', {'status': 'ok'}, ('nested_tuple', 'one_more'))


def func(number: int):
    i = 10
    res = 1
    while i > 0:
        i -= 1
        res += res
    return res


if __name__ == '__main__':
    test_parsers(dic)
    test_parsers(lst)
    test_parsers(tupl)
    test_parsers(func)
