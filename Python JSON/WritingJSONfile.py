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
print(data)
with open("people.json","w") as file:
    json.dump(data,file)
