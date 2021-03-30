import json
with open("people.json") as file:
    people = json.load(file)
print(people)