library("plyr")
library("likert")

levels = c("Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree")

likert_df <- read.csv("~/Desktop/atdx_likert_data.csv")

likert_df[] <- lapply(likert_df, function(x) factor(x, levels = levels))

likert_df <- rename(likert_df, c(Q1 = "Q4: By looking individually at each project: The radar-chart values reflect the project's current state of architectural debt",
                                 Q2 = "Q5: By looking at all projects together: The radar charts reflect the differences in architectural debt present in the projects",
                                 Q3 = "Q6: The architectural debt types displayed in the radar-chart are a good representation of architectural debt",
                                 Q4 = "Q8: The results displayed in the radar charts inspire me to take action"))

likert_df = likert(likert_df)

#plot(likert_df, high.color = "#51B0FA", low.color = "#2F6798") + theme(text = element_text(family = "Times"))
plot(likert_df, high.color = "#238823", low.color = "#D2222D",
     group.order = names(likert_df$items), 
     centered = TRUE,
     text.color = "black",
     legend = "Reponse",
     legend.position = "right", panel.arrange = "v",
     plot.percents = TRUE, plot.percent.neutral = TRUE, 
     plot.percent.low = FALSE, plot.percent.high = FALSE, 
     text.size = 2.3) #+ theme(text = element_text(family = "Times", face="bold") )
