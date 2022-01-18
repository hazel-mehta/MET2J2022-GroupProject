import json
alph = ['A']# 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
                    athlete["Name"] = person["title"]
                    year = (person["ontology/birthDate"]).split('-')
                    athlete["Birth Year"] = year[0]
                    athlete["Sport"] = occupation_athlete[2]
                
                    gender = 'male'
                    if 'ontology/college_label' in person:
                        for element in person['ontology/college_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                    elif 'ontology/nationalTeam_label' in person:
                        for element in person['ontology/nationalTeam_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                    elif 'ontology/team_label' in person:
                        for element in person['ontology/team_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                                            
                    athlete["Gender"] = gender
                    summary_athletes.append(athlete)
print(summary_athletes)
                
import csv
keys = summary_athletes[0].keys()
with open("athletes_summary.csv", "w", encoding = 'utf8') as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(summary_athletes)