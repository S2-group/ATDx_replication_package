library(ggplot2)
library(reshape2)
library(Hmisc)
library(stats)
#library(wesanderson)

#pal <- wes_palette("Cavalcanti1", 100, type = "continuous")

cormatrix = rcorr(as.matrix(radar_data), type='spearman')

cordata = melt(cormatrix$r)
ggplot(cordata, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile() + xlab("") + ylab("") + theme(text = element_text(size = 18), 
                                            axis.text.x = element_text(angle = 45, hjust = 1),
                                            legend.text=element_text(size=13), 
                                            legend.title=element_text(size=15)) +
  guides(fill=guide_legend(title=" \u03C1")) +
  scale_fill_continuous(high = "#132B43", low = "#56B1F7")

  
