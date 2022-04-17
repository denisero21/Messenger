import os
from serializer.parsers.parser import Parser


def test_parsers(obj):
    path = 'parsed_files'
    # toml parser
    toml_parser = Parser.create_parser('toml')
    with open(os.path.join(path, 'parsed.toml'), 'w') as file:
        toml_parser.dump(obj, file)

    with open(os.path.join(path, 'parsed.toml'), 'r') as file:
        unparsed = toml_parser.load(file)
        print(f'toml parser result: {unparsed}')

    # yaml parser
    yaml_parser = Parser.create_parser('yaml')

    with open(os.path.join(path, 'parsed.yaml'), 'w') as file:
        yaml_parser.dump(obj, file)

    with open(os.path.join(path, 'parsed.yaml'), 'r') as file:
        unparsed = yaml_parser.load(file)
        print(f'yaml parser result: {unparsed}')

    # json parser
    json_parser = Parser.create_parser('json')
    with open(os.path.join(path, 'parsed.json'), 'w') as file:
        json_parser.dump(obj, file)

    with open(os.path.join(path, 'parsed.json'), 'r') as file:
        unparsed = json_parser.load(file)
        print(f'json parser result: {unparsed}')
    print()
