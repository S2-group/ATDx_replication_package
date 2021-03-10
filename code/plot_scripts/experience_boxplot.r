p <- qplot(y=survey_responses$Experience, x= 1, geom = "boxplot",
           ylab = "Experience (Years)") #fill="orange"
p + coord_flip() + theme(axis.title.y=element_blank(),
                          axis.text.y=element_blank(),
                          axis.ticks.y=element_blank()) +
  scale_y_continuous(breaks = seq(0, 30, by = 5)) +
  scale_x_continuous(breaks = NULL)