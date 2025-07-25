import json

json_data = '{"Name": "Iva", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))

data = {
    "Name": "ANA",
    "age": 20,
    "is_student": True
}
json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json","r",encoding="utf-8") as file:
    redata = json.load(file)
    print(data, type(data))

with open("json_user.json", "w",encoding="utf-8") as file:
   json.dump(data, file, indent=4, ensure_ascii=False)