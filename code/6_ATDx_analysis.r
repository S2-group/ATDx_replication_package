setwd("")
library(readr)
library(dplyr)
library(scales)
library(Ckmeans.1d.dp)

architectural_rules <- read_csv("ar_rules.csv")
filtered_dataset <- read_csv("apache_ATDx_input.csv")

drs <- architectural_rules$id
granularities <- architectural_rules$granularity_level

for (i in 1:length(drs)){
  dr = drs[i]
  granularity = granularities[i]
  
  # create weighted value of architectural rule for each project
  avgCol = paste("AVG", dr, sep = "")
  filtered_dataset[, avgCol] <- (filtered_dataset[, dr] / filtered_dataset[, granularity])
  filtered_dataset[is.na(filtered_dataset)] <- 0
  
  num_clusters = (min(6,n_distinct(filtered_dataset[,avgCol])))
  kCol = paste("K", dr, sep = "")
    
  x <- as.numeric(unlist(filtered_dataset[,avgCol]))
  
  ar_kmeans <- Ckmeans.1d.dp(x, k=c(0,num_clusters))
  
  filtered_dataset[, kCol] <- rank(ar_kmeans$centers)[ar_kmeans$cluster]
  
  filtered_dataset[, kCol] <- ((5*(filtered_dataset[, kCol] - min(filtered_dataset[, kCol])) / (max(filtered_dataset[, kCol]) - min(filtered_dataset[, kCol]))+0))
} 

filtered_dataset[is.na(filtered_dataset)] <- 0

filtered_dataset$inheritance <- (filtered_dataset$`Kjava:S1113` + filtered_dataset$`Kjava:S1161`
                                 + filtered_dataset$`Kjava:S1182` + filtered_dataset$`Kjava:S1185`
                                 + filtered_dataset$`Kjava:S1210` + filtered_dataset$`Kjava:S2062`
                                 + filtered_dataset$`Kjava:S2157` + filtered_dataset$`Kjava:S2638`
                                 + filtered_dataset$`Kjava:S2975`)/9

filtered_dataset$exception <- (filtered_dataset$`Kjava:S1130`+ filtered_dataset$`Kjava:S1165`
                                + filtered_dataset$`Kjava:S2166` + filtered_dataset$`Kjava:S112`)/4

filtered_dataset$vmsmell <- (filtered_dataset$`Kjava:S1210`+ filtered_dataset$`Kjava:S1217`
                              + filtered_dataset$`Kjava:S2157` + filtered_dataset$`Kjava:S2638`
                              + filtered_dataset$`Kjava:S2975`)/5

filtered_dataset$interface <- (filtered_dataset$`Kjava:S107` + filtered_dataset$`Kjava:S1104`
                               + filtered_dataset$`Kjava:S1118` + filtered_dataset$`Kjava:S1133`
                               + filtered_dataset$`Kjava:S1610`)/5

filtered_dataset$threading <- (filtered_dataset$`Kjava:S2222` + filtered_dataset$`Kjava:S2236`
                                + filtered_dataset$`Kjava:S2273`+ filtered_dataset$`Kjava:S2276`
                                + filtered_dataset$`Kjava:S2885`)/5


filtered_dataset$complexity <- (filtered_dataset$`Kjava:S1133` + filtered_dataset$`Kjava:S1199`)/2

filtered_dataset$ATDx <- (filtered_dataset$inheritance + filtered_dataset$exception + filtered_dataset$vmsmell +
                          filtered_dataset$interface + filtered_dataset$threading + filtered_dataset$complexity)/6

write.csv(filtered_dataset, file="apache_ATDx_CkMeans_final_output.csv", row.names = TRUE)
