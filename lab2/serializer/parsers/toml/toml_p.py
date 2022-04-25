import toml
standard_types = ["int", "float", "bool", "str", "None"]
transfer = "\n"
gap_symbols = "\n\r\t "


class TomlParser:
    def dumps(self, obj):
        self.replace_null(obj)
        return toml.dumps(obj)

    def dump(self, obj, fp):
        fp.write(self.dumps(obj))

    def loads(self, s):
        res = toml.loads(s)
        self.replace_null_back(res)
        return res

    def load(self, fp):
        return self.loads(fp.read())

   
    def replace_null(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if value is None:
                    obj[key] = "null"
                self.replace_null(value)
        if isinstance(obj, list):
            for i in range(len(obj)):
                if obj[i] is None:
                    obj[i] = "null"
                self.replace_null(obj[i])

    def replace_null_back(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if value == "null":
                    obj[key] = None
                else:
                    self.replace_null_back(value)

        if isinstance(obj, list):
            for i in range(len(obj)):
                if obj[i] == "null":
                    obj[i] = None
                else:
                    self.replace_null_back(obj[
