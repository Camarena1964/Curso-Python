person = {
    "name" : ["Sandra"],
    "last_name" : ["Camarena"],
    "second_last": ["De La Mora"],
    "age" : ["29"]
}
for key, value in person.items():
    print (key, value)

person.update({"citizenship" : "Mexicana"})
for key, value in person.items():
    print (key, value)