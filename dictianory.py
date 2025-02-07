costumer = { "name": "feri", "age": 20, "is_verified": True }
name = costumer["name"]
age = costumer["age"]
is_verified = costumer["is_verified"]

for key in costumer:
    value = costumer[key]
    print(f"{key} : {value}")
    
# cara lain
costumer = { "name": "feri", "age": 20, "is_verified": True }
name = costumer["name"]
age = costumer["age"]
is_verified = costumer["is_verified"]

for key, value in costumer.items():
    print(f"{key} : {value}")