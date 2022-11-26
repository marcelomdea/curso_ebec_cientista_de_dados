from sys import argv

import extracao
import visualizacao

# Gerando arquivo csv com sa taxa CDI do site da B3

extracao.gerar_arquivo_taxa_cdi_csv()

# Criar/salvar arquivo png do gráfico

visualizacao.gerar_grafico(argv[1])