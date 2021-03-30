import json
people_string= '''{
    "people":[
            {
                "name": "Shuvro",
                "email":"shuvro@gmail.com",
                "age" : 20,
                "gender":"Male",
                "beard": null,
                "license" : true
            },
            {
                "name": "Krishna",
                "email":"krishna@gmail.com",
                "age" : 18,
                "gender":"Male",
                "beard": null,
                "license" : false
            }
        ]
}'''
data = json.loads(people_string)
for person in data["people"]:
    person.pop("beard")
p_string = json.dumps(data, indent=2, sort_keys=True)
print(p_string)

