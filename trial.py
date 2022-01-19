import json

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
summary_athletes = []

for letter in alph:
    with open(f'People/{letter}_people.json') as file:
        # 'Group_Repo' is a filename dependent on who is running the code. This is for Hazel's file location
        # it was cool to be able to use the f string function for more than just print. Proved super useful here!

        text = json.load(file)
        
        for person in text:
            occupation_athlete = (person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label'])
            # the label of 'occupation_label' appear this way in the data set

            if 'athlete' in occupation_athlete:
                athlete = {}
                # dictionary defined within the 'if' loop so we can create a new dictionary for each athlete. 
                # This will get added to the main list before looking into the next athlete.
                
                if 'ontology/birthDate' in person and type(person["ontology/birthDate"]) is str:
                # string dates were considered because of discrepencies in the data in the field of 'birthDate'

                    athlete["Name"] = person["title"]
                    # making a key to our new dictionary to match the title of the line of the data set (athlete's name)

                    year = (person["ontology/birthDate"]).split('-')
                    # in the form 'Year-Month-Day' in 'birthDate'
                    # we wanted to sperate the year from the rest of the date for our data collection
                    athlete["Birth_Year"] = year[0]
                    # new key for the dictionary

                    # to add information to the next key: "Sport" this next set of the code was needed
                    # this is because of the way the data set was set up with information about the athletes' sports in different fields
                    if occupation_athlete[2] == "athlete":
                        athlete["Sport"] = occupation_athlete[3]
                        if occupation_athlete[3] == "Q5":
                           athlete["Sport"] = occupation_athlete[2] 
                    else:
                        athlete["Sport"] = occupation_athlete[2]
                
                    # to set up the next key about gender we define them as unspecified unless proven otherwise
                    gender = 'unspecified'
                    if 'ontology/college_label' in person:
                        for element in person['ontology/college_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                            elif 'men' in element or 'male' in element:
                                gender = "male"
                    elif 'ontology/nationalTeam_label' in person:
                        for element in person['ontology/nationalTeam_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                            elif 'men' in element or 'male' in element:
                                gender = "male"
                    elif 'ontology/team_label' in person:
                        for element in person['ontology/team_label']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                            elif 'men' in element or 'male' in element:
                                gender = "male"
                    elif 'http://purl.org/dc/elements/1.1/description' in person:
                        for element in person['http://purl.org/dc/elements/1.1/description']: 
                            if 'women' in element or 'female' in element:
                                gender = "female"
                            elif 'men' in element or 'male' in element:
                                gender = "male"          
                                            
                    athlete["Gender"] = gender

                    # now we can add the individual athlete's dictionary to the main list 'summary_athletes'!
                    summary_athletes.append(athlete)

# we now have a list of dictionaries with all the data we need about each athlete
# this data now includes: Name, Birth_Year, Sport, Gender

# we are now ready to save this data in a csv file so we can use it in RStudio for visualization and further analysis!
import csv
keys = summary_athletes[0].keys()
with open("athletes_summary.csv", "w", newline = "", encoding = 'utf8') as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(summary_athletes)

