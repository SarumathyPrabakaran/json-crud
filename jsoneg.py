import json

f = open("jsoneg2.json","w")

# data = json.load(f)

# print(data)

# f1 = open("jsoneg1.json","w")


dic = {
    "key": "value",
    "key2": "value",
    "key3": "value"
}

json.dump(dic,f)

# print("success")

# data = json.load(f)

# print(data)

# #update json file

# f1 = open("jsoneg1.json","w")

# new_data = {"key3": "value"}


# data.update(new_data)

# print(data)
# json.dump(data,f1)