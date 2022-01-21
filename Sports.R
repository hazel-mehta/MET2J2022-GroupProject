library('tidyverse')

#making a variable for total athletes in the data set
athletes <- read_csv('comparative_gender_athletes.csv') %>%
total_athletes = nrow(athletes)

#calculating the proportion of total athletes labeled per gender - used for the report table 1
percentage_gender_total <- group_by(athletes, Gender) %>%
  summarize(proportion <- (n()/total_athletes)*100) 

#percentages of total athletes per gender in new data set - used for the report table 1
percentage_new_gender_total <- group_by(athletes, Replaced_Gender)%>%
  summarize(proportion = (n()/total_athletes)*100) 

#grouping by Sport to calculate total number of athletes per sport 
#used both for plot not included and Final Plot
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
          )%>%
#pivot wider was used for the final plot, to merge the tables, and not for the unused plots 
  pivot_wider(names_from = Gender, values_from = proportion_sport)


#with new data set, grouping by Sport to calculate total number of athletes per sport - 
#used for both unicluded plot and Final Plot
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
  ) %>%
#pivot wider was used to merge both tables for the new plot, the unused plots didn't use this pivot
  pivot_wider(names_from = Replaced_Gender, values_from = new_proportion_sport)

#Joining both plots to calculate relative proportions for Final Plot
percentage_gender_sport_both <- percentage_gender_sport %>%
  left_join(new_percentage_gender_sport)

#Final Plot comparing both data sets by sport and by gender both labelled and more accurate
plot_both <- percentage_gender_sport_both %>%
  pivot_longer(c(everything(), -Sport), names_to='gender') %>%
  mutate(group = ifelse(gender == 'male' | gender == 'female', 'Labeled Gender', 'Real Gender')) %>%
  mutate(gender = str_to_lower(gender)) %>%
  ggplot() +
  geom_col() +
  aes(x = group, y = value, fill = gender) +
  labs(x = NULL, y = 'Proportion') +
  facet_wrap(~Sport)

ggsave('Diference_both_athlete.pdf', plot_both)

#UNUSED PLOT
#plotting proportion of total labelled athletes per sport per gender
labeled_gender <- ggplot(data = percentage_gender_sport) +
  aes(x = Sport, y = proportion_sport, fill = Gender) +
  geom_col(position = 'dodge') +
  theme_light() +
  labs(x = 'Sport', y =  'Proportion of Gender Labelled')

ggsave('Barplot_gender_labels_athlete.pdf', labeled_gender)

#UNUSED PLOT
#new data set, plotting proportion of total athletes per sport per gender
real_athlete_gender <-ggplot(data = new_percentage_gender_sport) +
  aes(x = Sport, y = new_proportion_sport, fill = Replaced_Gender) +
  scale_fill_discrete(name = 'Gender', labels = c('female', 'male')) +
  geom_col(position = 'dodge') +
  theme_light() +
  labs(x = 'Sport', y =  'Proportion of Gender')

ggsave('Barplot_gender_new_labels_athlete.pdf', real_athlete_gender, width = 7.93, height = 5.92)


