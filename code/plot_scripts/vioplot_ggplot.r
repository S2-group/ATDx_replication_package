library(readr)
library(tidyr)
library(ggplot2)
library(dplyr)
df <- read_csv("~/Documents/PhD/SVN_Roberto_VU/ATDx_validation/data/apache_ATDx_ckMeans_final_output.csv")

viodata <- df[, c('interface', 'inheritance', 'exception',
                  'vmsmell', 'threading', 'complexity',
                  'ATDx')]



names(viodata)[names(viodata) == "interface"] <- "Interface"
names(viodata)[names(viodata) == "inheritance"] <- "Inheritance"
names(viodata)[names(viodata) == "vmsmell"] <- "JVMS"
names(viodata)[names(viodata) == "exeption"] <- "Exception"
names(viodata)[names(viodata) == "threading"] <- "Threading"
names(viodata)[names(viodata) == "complexity"] <- "Complexity"

# viodata <- factor(viodata, levels=c("Interface", "Inheritance", "JVMS", "Exception", 
#                                    "Threading", "Complexity", "ATDx"), ordered=TRUE)

p <- viodata %>% 
  gather(key="ATDD", value="Value") %>%
  ggplot( aes(x=ATDD, y=Value, fill=ATDD)) +
  geom_violin(width=1) + 
  scale_fill_manual(values=c("#F76B62", "#F76B62", "#F76B62", 
                             "#F76B62", "#F76B62", "#F76B62",
                             "#F76B62")) +
  theme(legend.position = "none") +
  geom_boxplot(width=.025, outlier.colour=NA, color="black", fatten=2)
  
plot(p)


# library(vioplot)
# 
# #vioplot(onap_ATDx_CkMeans_final_output$Interface, onap_ATDx_CkMeans_final_output$Inheritance, onap_ATDx_CkMeans_final_output$Exception, onap_ATDx_CkMeans_final_output$JVMS, onap_ATDx_CkMeans_final_output$Threading, onap_ATDx_CkMeans_final_output$Complexity, onap_ATDx_CkMeans_final_output$ATDx, names=c("Interface", "Inheritance", "Exception", "JVMS", "Threading", "Complexity", "ATDx"), col = c("#51B0FA", "#51B0FA", "#51B0FA","#51B0FA","#51B0FA","#51B0FA", "blue"))
# vioplot(onap_ATDx_CkMeans_final_output$interface, onap_ATDx_CkMeans_final_output$inheritance, onap_ATDx_CkMeans_final_output$exception,
#         onap_ATDx_CkMeans_final_output$vmsmell, onap_ATDx_CkMeans_final_output$threading, onap_ATDx_CkMeans_final_output$complexity,
#         onap_ATDx_CkMeans_final_output$ATDx, 
#         names=c("Interface", "Inheritance", "Exception", "JVMS", 
#                 "Threading", "Complexity", "ATDx"), 
#         col = c("#00B7BC", "#00B7BC", "#00B7BC","#00B7BC","#00B7BC",
#                 "#00B7BC", "#FFA500")
# )
# title(ylab="Value", xlab="ATDD")
# grid(NULL, lty = 20, col = "grey", nx=0)
