import json

info_dic = {"name": "신짱구", "birth" : "1224", "age" : 10}
info_data = json.dumps(info_dic, indent = 4, ensure_ascii = False)
print(info_data)

info_out = json.loads(info_data)
print(info_out)

num_list = json.dumps([], indent = 4)
print(num_list)