#Accessing into Dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(person["name"])#Alice

print(person.get("age"))#30
print(person.get("country", "Empty"))#Unknown(default)
country = person.get("country")
if country == None:
    country = "Empty inside IF"
print(country)
print(person["country"])
#print(person["country"]) this code will give error due to cannot find the key in dict

user = {}
user["username"] = "Soknoy"
user.update9({"password": 123456, "username": "Soknoy Update", "capcha": "12345"})
user.setdefault("username", "Soknoy") #setdefault value add only the key not exist it will not update 
user.setdefault("age", 10)
print(user)

# how to remove it
removeValue = user.pop("username")
print(removeValue)
print(user)

removeValue = user.pop("username")
print(removeValue)
print(user)

#How to iterate over dictionaries

#Looping through key
for key in user:
    print(f'Key is {key} Value is {user[key]}')

#Looping through items can get both key, value from item 
print("-_______________________________________________")
for key, val in user.items():
    print(f'Key is {key} Value is {val}')

#Looping through dict using only value
print("-_______________________________________________")
for val in user.values():
    print(f'Value is {val}')
    







