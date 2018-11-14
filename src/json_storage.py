import json


class JSONStorage(object):
    def __init__(self, file_path):
        self.file_path=file_path
    def store(self, dict):
        with open(self.file_path, 'w') as file:
            str_dict = str(dict)
            str_dict_q=''
            for i in range(len(str_dict)):
                if str_dict[i]=="'":
                    str_dict_q=str_dict_q+'"'
                else:
                    str_dict_q=str_dict_q+str_dict[i]
            file.write(str_dict_q)

    def load(self):
        with open(self.file_path, 'r') as file:
            try:
                return json.load(file)
            except:
                return {}