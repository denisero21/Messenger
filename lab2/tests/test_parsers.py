import os
from serializer.parsers.parser import Parser


def test_parsers(obj, is_func=False, formt=None):
    path = 'parsed_files/'

    # json parser
    serializer = Parser('json')
    with open(os.path.join(path, 'parsed.json'), 'w') as file:
        serializer.dump(obj, file)
    with open(os.path.join(path, 'parsed.json'), 'r') as file:
        result = serializer.load(file)
    if not is_func:
        print(f'json parser result: {result}')
    elif formt == 'json':
        return result

    # toml parser
    serializer = Parser('toml')
    with open(os.path.join(path, 'parsed.toml'), 'w') as file:
        serializer.dump(obj, file)
    with open(os.path.join(path, 'parsed.toml'), 'r') as file:
        result = serializer.load(file)
    if not is_func:
        print(f'toml parser result: {result}')
    elif formt == 'toml':
        return result

    # yaml parser
    serializer = Parser('yaml')
    with open(os.path.join(path, 'parsed.yaml'), 'w') as file:
        serializer.dump(obj, file)
    with open(os.path.join(path, 'parsed.yaml'), 'r') as file:
        result = serializer.load(file)
    if not is_func:
        print(f'yaml parser result: {result}')
    elif formt == 'yaml':
        return result
    print()