library('tidyverse')

athletes <- read_csv('athletes_summary.csv')
total_athletes = nrow(athletes)

percentage_gender_total <- group_by(athletes, Gender)%>%
  summarize(proportion = (n()/total_athletes)*100) 

percentage_gender_sport <- group_by(athletes, Sport)%>%
  mutate(sport_total = n()) %>%
  ungroup()%>%
  group_by(Gender, Sport) %>%
  summarize(proportion_sport = (n()/mean(sport_total))*100) %>%
  filter(
          (Sport == 'soccer player' |
           Sport == 'basketball player' |
           Sport == 'golf player'| 
           Sport == 'volleyball player') &
           (Gender == 'female'|
              Gender == 'male')
          )

ggplot(data = percentage_gender_sport) +
  aes(x = Gender, y = proportion_sport, fill = Sport) +
  geom_col(position = 'dodge')
  