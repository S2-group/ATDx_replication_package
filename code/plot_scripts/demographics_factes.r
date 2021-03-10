library(readr)
library(ggplot2)
library(facetscales)
library(ggthemes)

dem <- read_csv("Documents/PhD/SVN_Roberto_VU/ATDx_validation/data/merged_portfolios_demographics.csv")
dem$type <- factor(dem$type , levels=c("Java NCLOC", "Java Files", "Java Classes", "Java Functions"))
p <- ggplot(data = dem, aes(x=type, y=value)) + geom_boxplot(aes(fill=Ecosystem))

type_names <- list(
  "Java NCLOC"="Java NCLOC",
  "Java Files"="Java Files",
  "Java Classes"="Java Classes",
  "Java Function"="Java Functions"
)

type_labeller <- function(variable,value){
  return(type_names[value])
}

p + theme(axis.text.x = element_blank()) + 
  facet_wrap( ~ type, scales="free",  labeller = type_labeller) +
  scale_y_log10() + ylab("log10 value") + xlab("") + theme_bw() +
  theme(strip.text.x = element_blank(), strip.background = element_blank(),
  axis.text=element_text(size=10), axis.title=element_text(size=12))
  



