library('tidyverse')

athletes<- read_csv('athletes_summary.csv')
total_athletes = nrow(athletes) 
summarized_athletes <- group_by(athletes, Gender, Sport)%>%
  summarize(proportion = (n()/total_athletes)*100)
  
ggplot(data = summarized_athletes) +
  aes(x = Sport, y = proportion, fill = Gender) +
  geom_col()
  