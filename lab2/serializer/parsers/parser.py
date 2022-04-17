from serializer.parsers.json.json import JsonParser
from serializer.parsers.yaml.yaml import YamlParser
from serializer.parsers.toml.toml import TomlParser


class Parser:

    @staticmethod
    def create_parser(name: str):
        name = name.lower()
        if name == "json":
            return JsonParser()
        elif name == "yaml":
            return YamlParser()
        elif name == "toml":
            return TomlParser()
        else:
            raise ValueError
