# Defindo diretorio

setwd("~/R/imagens")

# acrregar library

library("TCGAbiolinks")
library(dplyr)


## fazer a busca do projeto e dados

  # Tissue slide image files from legacy database
  Primeira_imagem_teste <- GDCquery(project = "TCGA-STAD", 
                         data.category = "Biospecimen", 
                         data.type = "Slide Image",
                         experimental.strategy = "Diagnostic Slide",
                         barcode = "TCGA-RD-A8N4") 
  query.harmonized  %>% 
    getResults %>% 
    head  %>% 
    DT::datatable(options = list(scrollX = TRUE, keys = TRUE))
  
  
   
  # Download images formado SVS
  
  
  GDCdownload(Primeira_imagem_teste)

  