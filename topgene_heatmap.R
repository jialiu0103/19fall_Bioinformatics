

selectg=gene_exp[-which(gene_exp$log2.fold_change. == Inf),]
selectg=selectg[-which(selectg$log2.fold_change. == -Inf),]
selectg=selectg[-which(selectg$significant == 'no'),]
selectg=selectg[c('gene', 'log2.fold_change.','gene_id')]
selectg$abs_diff=abs(selectg$log2.fold_change.)
selectg[order(selectg$abs_diff, decreasing= T), ]
topgene=selectg[1:1000,]
topg=topgene[c('gene','gene_id')]


#get top 1000 genes from p0_1
samplep0=genes[c('gene_id','P0_FPKM','gene_short_name')]
sam1=samplep0[which(samplep0$gene_id %in% topg$gene_id),]
sam1[order(sam1$gene_short_name), ]

#get other 7 samples top genes
supplement_2 <- NIHMS647083_supplement_2[which(NIHMS647083_supplement_2$GeneID %in% topg$gene),]
gid=supplement_2[c('Gene','GeneID')]
gid[order(gid$Gene), ]
samother=fpkm_matrix[which(fpkm_matrix$tracking_id %in% gid$Gene),]
news=samother[!duplicated(samother$tracking_id), ]
news[order(news$tracking_id), ]
news$name=gid$GeneID

#make 2 tables in same dim
sam1=sam1[which(sam1$gene_short_name %in% news$name),]
sam1$name=sam1$gene_short_name
news=news[which(news$name %in% sam1$gene_short_name),]
sam1[order(sam1$gene_short_name), ]
allsam=merge(x = news, y = sam1, by = "name", all = TRUE) 
allsam= na.omit(allsam)
sam=allsam[c('name','P0_FPKM',"P0_2_FPKM", "P4_1_FPKM" ,"P4_2_FPKM" ,"P7_1_FPKM","P7_2_FPKM",'Ad_1_FPKM',"Ad_2_FPKM")]
row.names(sam) <- make.names(sam[,1],TRUE)
sam=sam[,-1]

names(sam)[names(sam) == "P0_FPKM"] <- "P0_1"
names(sam)[names(sam) == "P0_2_FPKM"] <- "P0_2"
names(sam)[names(sam) == "P4_1_FPKM"] <- "P4_1"
names(sam)[names(sam) == "P4_2_FPKM"] <- "P4_2"
names(sam)[names(sam) == "P7_1_FPKM"] <- "P7_1"
names(sam)[names(sam) == "P7_2_FPKM"] <- "P7_2"
names(sam)[names(sam) == "Ad_1_FPKM"] <- "Ad_1"
names(sam)[names(sam) == "Ad_2_FPKM"] <- "Ad_2"

sam_matrix=data.matrix(sam)
mode(sam_matrix) <- 'numeric'
heatmap(sam_matrix,scale = 'row',Colv = NA)
heatmap(sam_matrix,scale = 'row')
