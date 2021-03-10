library(vioplot)
library(readr)
paper_dataset <- read_csv("~/Documents/PhD/SVN_Roberto_VU/ATDx_validation/data/onap_ATDx_ckMeans_final_output.csv")


#vioplot(paper_dataset$Interface, paper_dataset$Inheritance, paper_dataset$Exception, paper_dataset$JVMS, paper_dataset$Threading, paper_dataset$Complexity, paper_dataset$ATDx, names=c("Interface", "Inheritance", "Exception", "JVMS", "Threading", "Complexity", "ATDx"), col = c("#51B0FA", "#51B0FA", "#51B0FA","#51B0FA","#51B0FA","#51B0FA", "blue"))
vioplot(paper_dataset$interface, paper_dataset$inheritance, paper_dataset$exception,
        paper_dataset$vmsmell, paper_dataset$threading, paper_dataset$complexity,
        paper_dataset$ATDx, 
        names=c("Interface", "Inheritance", "Exception", "JVMS", 
                "Threading", "Complexity", "ATDx"), 
        col = c("#00B7BC", "#00B7BC", "#00B7BC","#00B7BC","#00B7BC",
                 "#00B7BC", "#FF9B00"))
        # col = c("#F76B62", "#F76B62", "#F76B62","#F76B62","#F76B62",
        # "#F76B62", "#FF9B00"))
title(ylab="Value", xlab="ATDD")
grid(NULL, lty = 20, col = "grey", nx=0)