# Relatório de Aplicação e Funcionamento do Processo Completo

Relatório que aborda todo o processo de instalação de programas, download de imagens, anotação de imagens e extração das características anotadas de cada imagem.

Parte I

### **1. Instalação Quick Annotator (QA)**

A instalação do programa, assim com sua utilização, está detalhada no relatório com título [Relatório Quick Annotator](https://docs.google.com/document/d/1MCoDmCgpUCUB7PunPNNoLTGoftO0xp7thU4_1iiiUB8/edit#heading=h.i76d10rspvdl).

### **2. Download das Imagens TCGA**

Para se fazer o download das imagens WSI é preciso baixar o RStudio e abrir o script `TCGA_Imagens_dowload.R` e colocar o nome da imagem desejada no parâmetra _barcode_ da função _GDCquery._ Como mostrado abaixo:

![A imagem não pode ser carregada!](https://drive.google.com/file/d/1gvr48Kr6HbP4cr4nqlea-OATr154fpQ_/view?usp=sharing)

A lista de imagens pode ser encontrada na planilha **v1 Seleção Especialista Colunas Filtrada + stad tcga 2018 clinical data.xlsx** disponível neste [link (Drive)](https://docs.google.com/spreadsheets/d/1K2IdILznDx-GR7o6Py-dkn-G8PMdOrjz/edit#gid=1676572784). Nem todas as imagens podem ser baixadas. O código retorna uma lista das imagens disponíveis quando se tenta baixar uma imagem que não está presente na mesma. Atualmente (18/01/2023) não se consegue baixar imagens muito grandes (acima de 800 Mb).

Parte II

### **1. Extração dos _Patches_ de WSI**

O QA disponibiliza um script para a divisão das imagens WSI em _patches_ com o nome `extract_tiles_from_wsi_openslide.py` cujo o uso é descrito no [Relatório Quick Annotator](https://docs.google.com/document/d/1MCoDmCgpUCUB7PunPNNoLTGoftO0xp7thU4_1iiiUB8/edit#heading=h.i76d10rspvdl) já citado. Para se realizar esta operação em múltiplas imagens é possível utilizar o script `mult_extract_tiles.py` presente na pasta [Anotation](https://drive.google.com/drive/folders/1lHYTMcQgypkCy0Y1CCXw6YUBhvDW9WXq?usp=share_link)[Process Scripts](https://drive.google.com/drive/folders/1lHYTMcQgypkCy0Y1CCXw6YUBhvDW9WXq?usp=share_link) e seu uso está especificado no cabeçalho do código. Um exemplo é mostrado abaixo:

![A imagem não pode ser carregada!](https://drive.google.com/file/d/1YQl3pQhNCaj_FttU7zMG2HL7GesA9Fqm/view?usp=share_link)

### **2. Utilização do Quick Annotator**

A utilização do QA é explicada de forma detalhada nos tutoriais indicados no [Relatório Quick Annotator](https://docs.google.com/document/d/1MCoDmCgpUCUB7PunPNNoLTGoftO0xp7thU4_1iiiUB8/edit#heading=h.i76d10rspvdl). Essa pode ser resumida em alguns passos:

1. Criar um projeto.
2. Carregar as imagens no projeto.
3. Criar patches das imagens (botão _Make Patches_).
4. Treinar o primeiro modelo (botão _(Re)train Model 0_).
A partir daqui já se pode treinar um novo modelo fazendo anotações.
5. Fazer o agrupamento dos patches criados (botão _Embed Patches_)
Depois é possível visualizar esse agrupamento e escolher um patch para abrir uma imagem.
6. Fazer anotações (pelo menos 1 para treino e 1 para teste)
7. Treinar o modelo (botão _Retrain DL_ \> _From base_)
8. Refinar o modelo corrigindo as predições do modelo anterior com novas anotações.
9. Retreinar o modelo. Caso o resultado do modelo anterior tenha sido já perto do desejado, pode-se utilizar o botão _Retrain DL_ \> _From last_. Caso contrário, recomenda-se usar o mesmo do paço 7.
10. Uma vez que as anotações apresentam um resultado satisfatório pode-se baixar as máscaras das imagens.

### **3. Baixando as Máscaras da Imagens**

O processo de download das máscaras geradas pelo QA pode ser feito manualmente aguardando a predição da imagem ficar pronta indicado pela cor verde da _flag_ _Prediction_ e clicando-se no botão _Download_ \> _DL Result Image_. Esse mesmo processo pode ser feito automaticamente utilizando o notebook `Auto-QA.ipynb` , onde se encontra uma explicação detalhada do processo. O arquivo pode ser encontrado na pasta [Anotation Process Scripts](https://drive.google.com/drive/folders/1lHYTMcQgypkCy0Y1CCXw6YUBhvDW9WXq?usp=share_link).

### **4. Extraindo Regiões de Interesse das Imagens**

Uma vez que se é obtido as máscaras das imagens usa-se o script `image\_mask\_split.py` para extrair da imagens apenas as regiões anotadas. Esse script divide cada imagem em novos patches de tamanho especificado. Os detalhes do seu funcionamento estão documentados no cabeçalho do mesmo. O arquivo pode ser encontrado na pasta [Anotation Process Scripts](https://drive.google.com/drive/folders/1lHYTMcQgypkCy0Y1CCXw6YUBhvDW9WXq?usp=share_link).
