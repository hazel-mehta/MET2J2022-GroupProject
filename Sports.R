library('tidyverse')

#making a variable for total athletes in the dataset
athletes <- read_csv('athletes_summary.csv')
total_athletes = nrow(athletes)

#calculating the proportion of total athetes labeled per gender
percentage_gender_total <- group_by(athletes, Gender)%>%
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

#plotting proportion of total labelled athletes per sport per gender
ggplot(data = percentage_gender_sport) +
  aes(x = Sport, y = proportion_sport, fill = Gender) +
  geom_col(position = 'dodge') +
  theme_light() +
  labs(x = 'Sport', y =  'Proportion of Gender Labelled')

ggsave('Barplot_gender_labels_athlete.pdf')
