import json
summary_athletes_gender = []
gender_information = {}

with open ('wiki_genders.txt') as brandon_file:
    headers = brandon_file.readline()
    for line in brandon_file:
        wiki_id, gender, title = line.strip().split('\t')
        gender_information.update({title:gender})

# print(gender_information)

with open('athletes_dictionary.json') as file:
    athletes_text = json.load(file)
    for person in athletes_text:
        person_clean = person['Name'].replace('_', ' ')
        if person_clean in gender_information.keys():
            person['Replaced_Gender'] = gender_information[person_clean]
            #print(f"Replaced {person_clean}'s gender!")
        else:
            person['Replaced_Gender'] = 'unspecified'
        # if name[2] in person['Name']:
        #     person["Gender"] = name[1]
        summary_athletes_gender.append(person)
        


'''

with open('athletes_dictionary.json') as file:
    athletes_text = json.load(file)
    for name in gender_text:
        for person in athletes_text:
            (person['Name']).replace('_', ' ')
            if name[2] in person['Name']:
                person["Gender"] = name[1]
                summary_athletes_gender.append(person)
'''            

import csv
keys = summary_athletes_gender[0].keys()
with open("comparative_gender_athletes.csv", "w", newline = "", encoding = 'utf8') as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(summary_athletes_gender)

    