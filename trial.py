import json
alphabet = ['A']#, 'B', 'C', 'D']
athletes = []
for x in alphabet:
    with open(f'People/{x}_people.json') as file:
        text = json.load(file)
        for person in text:
            occupation_athlete = (person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label'])
            if 'basketball player' in occupation_athlete:
                athletes.append(person)

with open('athletes1.json','w') as file:
    json.dump(athletes, file)


gender = "female"
for person in athletes:
    if 'ontology/college_label' in person.keys():
        for element in person['ontology/college_label']: 
            if 'women' in element or 'female' in element:
                gender = "female"
    elif 'ontology/nationalTeam_label' in person.keys():
        for element in person['ontology/nationalTeam_label']: 
            if 'women' in element or 'female' in element:
                gender = "female"
    elif 'ontology/team_label' in person.keys():
        for element in person['ontology/team_label']: 
            if 'women' in element or 'female' in element:
                gender = "female"
    else: 
        gender = "male"
    
    if gender == 'female':
        print(gender)