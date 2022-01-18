import json
alph = ['A'] #'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
athletes = []
summary_athletes =[]

for letter in alph:
    with open(f'People/{letter}_people.json') as file:
        text = json.load(file)

        for person in text:
            occupation_athlete = (person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label'])
            

            if 'athlete' in occupation_athlete:
                athlete = {}
                athletes.append(person)
                if 'ontology/birthDate' in person and type(person["ontology/birthDate"]) is str:
                    year = (person["ontology/birthDate"]).split('-')
                    athlete["Birth Year"] = year[0]
                    athlete["Sport"] = occupation_athlete[2]
                    athlete["Name"] = person["title"]
                
                
                    if 'ontology/college_label' in person:
                        for element in person['ontology/college_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                                athlete["Gender"] = gender
                    elif 'ontology/nationalTeam_label' in person:
                        for element in person['ontology/nationalTeam_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                                athlete["Gender"] = gender
                    elif 'ontology/team_label' in person:
                        for element in person['ontology/team_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                                athlete["Gender"] = gender
                    else: 
                        gender = "male"
                        athlete["Gender"] = gender
                    
                    
                    summary_athletes.append(athlete)
                

with open ('tennis.json', 'w') as file:
    json.dump(summary_athletes, file)