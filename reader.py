import json


with open("pushup.json", 'r') as fh:
    data = json.load(fh)


print(data[0]["set1"])
print(len(data))

with open('pushup.json', 'w+') as fh:
    newdata = {'date': '12-20', 'set1': 32, 'set2': 22}
    data.append(newdata)
    json.dump(data, fh)