#ensure_ascii = False 한글 깨짐 방지
import json

with open("info1.json") as infile :
    data = json.load(infile)

print(data)

data_w = {"name" : "김철수", "birth" : "0101", "age" : 10}

with open("info1_w.json", "w") as outfile :
    json.dump(data_w, outfile, ensure_ascii = False)