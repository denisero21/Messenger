from serializer.serializer import serialize, deserialize
from serializer.parsers.json.json_p import JsonParser
from serializer.parsers.yaml.yaml_p import YamlParser
from serializer.parsers.toml.toml_p import TomlParser


class Parser:
    def __init__(self, parser_name):
        self.parser = self.create_parser(parser_name)

    @staticmethod
    def create_parser(name):
        name.lower()
        if name == 'json':
            return JsonParser()
        if name == 'toml':
            return TomlParser()
        if name == 'yaml':
            return YamlParser()
        raise ValueError

    def dumps(self, obj) -> str:
        ser = serialize(obj)
        dumped = self.parser.dumps(ser)
        return dumped

    def dump(self, obj, file):
        ser = serialize(obj)
        dumped = self.parser.dump(ser, file)
        return dumped

    def loads(self, obj: str):
        loaded = self.parser.loads(obj)
        des = deserialize(loaded)
        return des

    def load(self, file):
        loaded = self.parser.load(file)
        des = deserialize(loaded)
        return des
