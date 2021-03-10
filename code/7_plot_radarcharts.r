library(readr)
library(fmsb)
library(jpeg)

df <- read_csv("apache_ATDx_output.csv")

plot_redarchart <- function(df) {
    
plot_data <- as.data.frame(matrix(c(as.numeric(df["inheritance"]),as.numeric(df["exception"]), as.numeric(df["interface"]),
                               as.numeric(df["threading"]), as.numeric(df["vmsmell"]), as.numeric(df["complexity"])), ncol=6))

colnames(plot_data) <- c("Inheritance", "Exception" , "Interface" , "Threading" , "JVMS", "Complexity")

# Add 2 lines to the dataframe: the max and min of each topic to show on the plot
plot_data <- rbind(rep(5,2.5) , rep(0,2.5) , plot_data)

image_path <- file.path("plots", "ATDx_CkMeans", "apache", paste("ATDx_CkMeans_", df["projectKey"], ".jpg", sep = ""))

jpeg(file=image_path)

radarchart( plot_data  , axistype=1 ,

            seg=length(seq(min(plot_data),max(plot_data),1))-1,

            #custom polygon
            pcol=rgb(0.2,0.5,0.5,0.9) , pfcol=rgb(0.2,0.5,0.5,0.5) , plwd=5  ,

            #custom the grid
            cglcol="grey", cglty=1, axislabcol="grey", caxislabels=seq(0,6,1), cglwd=0.8,

            #custom labels
            vlcex=0.8,

            title = df["projectKey"]

)

dev.off()

}

apply(df, 1, plot_redarchart)