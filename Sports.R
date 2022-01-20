library('tidyverse')

#making a variable for total athletes in the data set
athletes <- read_csv('comparative_gender_athletes.csv') 
total_athletes = nrow(athletes)

#calculating the proportion of total athletes labeled per gender
percentage_gender_total <- group_by(athletes, Gender)%>%
  summarize(proportion = (n()/total_athletes)*100) 

#percentages of total athletes per gender in new data set
percentage_new_gender_total <- group_by(athletes, Replaced_Gender)%>%
  summarize(proportion = (n()/total_athletes)*100) 

#grouping by Sport to calculate total number of athletes per sport
percentage_gender_sport <- group_by(athletes, Sport)%>%
  filter(Gender == 'female' | Gender == 'male') %>%
  mutate(sport_total = n()) %>%
  ungroup()%>%
#grouping by gender and sport to obtain the proportion of each gender labeled per sport
  group_by(Gender, Sport) %>%
  summarize(proportion_sport = (n()/mean(sport_total))*100) %>%
#filtering to only contain sports that label both men and women to some degree
  filter(
          (Sport == 'soccer player' |
           Sport == 'basketball player' |
           Sport == 'golf player'| 
           Sport == 'volleyball player')
          )

#with new data set, grouping by Sport to calculate total number of athletes per sport
new_percentage_gender_sport <- group_by(athletes, Sport)%>%
  filter(Replaced_Gender == 'FEMALE' | Replaced_Gender == 'MALE') %>%
  mutate(sport_total = n()) %>%
  ungroup()%>%
  #grouping by gender and sport to obtain the proportion of each gender labeled per sport
  group_by(Replaced_Gender, Sport) %>%
  summarize(new_proportion_sport = (n()/mean(sport_total))*100)  %>%
  #filtering to only contain sports that label both men and women to some degree
  filter(
    (Sport == 'soccer player' |
       Sport == 'basketball player' |
       Sport == 'golf player'| 
       Sport == 'volleyball player')
  )

#plotting proportion of total labelled athletes per sport per gender
labeled_gender <- ggplot(data = percentage_gender_sport) +
  aes(x = Sport, y = proportion_sport, fill = Gender) +
  geom_col(position = 'dodge') +
  theme_light() +
  labs(x = 'Sport', y =  'Proportion of Gender Labelled')

ggsave('Barplot_gender_labels_athlete.pdf', labeled_gender)

#new data set, plotting proportion of total athletes per sport per gender
real_athlete_gender <-ggplot(data = new_percentage_gender_sport) +
  aes(x = Sport, y =new_proportion_sport, fill = Replaced_Gender) +
  scale_fill_discrete(name = 'Gender', labels = c('female', 'male')) +
  geom_col(position = 'dodge') +
  theme_light() +
  labs(x = 'Sport', y =  'Proportion of Gender')

ggsave('Barplot_gender_new_labels_athlete.pdf', real_athlete_gender, width = 7.93, height = 5.92)
