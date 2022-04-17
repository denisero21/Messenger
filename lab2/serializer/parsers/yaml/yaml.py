from serializer.serializer import Serializer
from serializer.parsers.yaml.yaml_serialization import serialize_yaml, deserialize_yaml


class YamlParser:

    @staticmethod
    def dumps(obj) -> str:
        obj = Serializer.serialize(obj)
        return serialize_yaml(obj)

    @staticmethod
    def dump(obj, file):
        file.write(YamlParser.dumps(obj))

    @staticmethod
    def loads(obj: str):
        obj = deserialize_yaml(obj)
        return Serializer.deserialize(obj)

    @staticmethod
    def load(file):
        return YamlParser.loads(file.read())