import json
with open('People/A_people.json') as file:
    text = json.load(file)

    athletes = []
    for person in text:
        occupation_athlete = (person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label'])
        if 'athlete' in occupation_athlete:
            athletes.append(person)
print(athletes)