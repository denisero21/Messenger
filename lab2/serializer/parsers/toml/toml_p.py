import toml
standard_types = ["int", "float", "bool", "str", "None"]
transfer = "\n"
gap_symbols = "\n\r\t "


class TomlParser:
    def dumps(self, obj):
        self.replace_null(obj)
        return toml.dumps(obj)
        # return self.inner_dumps(obj)

    def dump(self, obj, fp):
        fp.write(self.dumps(obj))

    def loads(self, s):
        res = toml.loads(s)
        self.replace_null_back(res)
        # print(res)
        return res

        # print(res)
        # return res

    def load(self, fp):
        return self.loads(fp.read())

    # def inner_dumps(self, obj, prefix=""):
    #     if type(obj).__name__ == "dict":
    #         res = ""
    #         flag_dicts = True
    #         for key, value in obj.items():
    #             if not isinstance(value, dict):
    #                 flag_dicts = False
    #             if self.is_standard(value):
    #                 res += key + " = " + self.obj_to_str(value) + transfer
    #
    #         for key, value in obj.items():
    #             if self.is_standard(value):
    #                 continue
    #             new_prefix = prefix
    #             if not prefix == "":
    #                 new_prefix += '.'
    #             new_prefix += key
    #             if not isinstance(value, list):
    #                 res += transfer + '[' + new_prefix + ']' + transfer
    #
    #             res += self.inner_dumps(value, new_prefix)
    #     if type(obj).__name__ == "list":
    #         res = ""
    #         for i in range(len(obj)):
    #             res += transfer + '[[' + prefix + ']]' + transfer + self.inner_dumps(obj[i], prefix)
    #     return res
    #
    # created = False
    #
    # def inner_loads(self, s):
    #     prev_path = ""
    #     res = {}
    #     is_dict = True
    #     current = 0
    #     lists_in_row = 0
    #     while True:
    #         line, current = self.read_line(s, current)
    #         if line is None:
    #             break
    #         line = self.trim(line)
    #         if line == "":
    #             continue
    #         if line[0:2] == "[[":
    #             prev_path = line[2:-2]
    #             is_dict = False
    #             self.created = False
    #             self.add(res, None, None, prev_path, is_dict, False)
    #             lists_in_row += 1
    #             if self.created:
    #                 lists_in_row = 0
    #             continue
    #         if line[0:1] == "[":
    #             prev_path = line[1:-1]
    #             is_dict = True
    #             lists_in_row = 0
    #             continue
    #         key, value = line.split("=")
    #         key = self.trim(key)
    #         value = self.str_to_obj(self.trim(value))
    #         # print(key, value)
    #         if lists_in_row == 2:
    #             self.add(res, key, value, prev_path, is_dict, True)
    #         else:
    #             self.add(res, key, value, prev_path, is_dict, False)
    #         # self.add(res, key, value, prev_path, is_dict, False)
    #         lists_in_row = 0
    #     return res
    #
    # def add(self, res, key, value, path, is_dict, new_flag):
    #     current = res
    #     if not path == "":
    #         sub_paths = path.split('.')
    #         for i in range(len(sub_paths)):
    #             if isinstance(current, dict):
    #                 if sub_paths[i] not in current:
    #                     if i == len(sub_paths) - 1:
    #                         if is_dict:
    #                             current[sub_paths[i]] = {}
    #                         else:
    #                             current[sub_paths[i]] = []
    #                     else:
    #                         current[sub_paths[i]] = {}
    #
    #                 current = current[sub_paths[i]]
    #             else:
    #                 flag = False
    #                 # for item in current:
    #                 if not new_flag:
    #                     if len(current) > 0 and sub_paths[i] in current[-1]:
    #                         current = current[-1][sub_paths[i]]
    #                         continue
    #                     # flag = True
    #                 if flag:
    #                     continue
    #                 if is_dict:
    #                     current.append({sub_paths[i]: {}})
    #                 else:
    #                     current.append({sub_paths[i]: []})
    #                 self.created = True
    #
    #                 current = current[-1][sub_paths[i]]
    #     if key is None:
    #         return
    #     if isinstance(current, dict):
    #         current[key] = value
    #     else:
    #         # if key == 'None' and value == None:
    #         #     current.append(None)
    #         # else:
    #         current.append({key: value})
    #
    #
    # def trim(self, s):
    #     l, r = -1, 0
    #     for i in range(len(s)):
    #         if l == -1 and not s[i] in gap_symbols:
    #             l = i
    #         if not s[i] in gap_symbols:
    #             r = i + 1
    #     return s[l:r]
    #
    # def read_line(self, s, current):
    #     if len(s) == current:
    #         return None, None
    #     res = ""
    #     while not s[current] == '\n':
    #         res += s[current]
    #         current += 1
    #     return res, current + 1
    #
    # def is_standard(self, value):
    #     if value is None or type(value).__name__ in standard_types:
    #         return True
    #     if isinstance(value, list):
    #         for i in range(len(value)):
    #             if value[i] is not None and not type(value[i]).__name__ in standard_types:
    #                 return False
    #         return True
    #     return False
    #
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
                    self.replace_null_back(obj[i])
    #
    # def add_double_slash(self, str):
    #     res = ""
    #     for i in range(len(str)):
    #         if str[i] == '\\':
    #             res += '\\\\'
    #         else:
    #             res += str[i]
    #     return res
    #
    # def obj_to_str(self, obj):
    #     if type(obj).__name__ == 'str':
    #         return "\"" + self.add_double_slash(str(obj)) + "\""
    #     if type(obj).__name__ == 'bool':
    #         return str(obj).lower()
    #     if obj == None:
    #         return "\"null\""
    #     if isinstance(obj, list):
    #         res = '['
    #         for i in range(len(obj)):
    #             res += self.obj_to_str(obj[i]) + ", "
    #         return res + ']'
    #     return str(obj)
    #
    # def str_to_obj(self, s):
    #     if s[0] == '[' and s[-1] == ']':
    #         res = []
    #         for item in s[1:-3].split(','):
    #             res.append(self.str_to_obj(self.trim(item)))
    #         return res
    #     # if s == '\"null\"':
    #     #     return None
    #     if s[0] == '"' and s[0] == s[-1]:
    #         return s[1:-1]
    #     if s == 'false':
    #         return False
    #     if s == 'true':
    #         return True
    #     try:
    #         return int(s)
    #     except:
    #         try:
    #             return float(s)
    #         except:
    #             return str(s)
