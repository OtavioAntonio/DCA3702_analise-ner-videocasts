# Análise de Co-ocorrência com NER em Videocasts
Este projeto aplica técnicas de Processamento de Linguagem Natural (NLP) para analisar transcrições de videocasts e identificar relações entre entidades nomeadas (pessoas, organizações e locais), gerando grafos de co-ocorrência para análise em ferramentas como Gephi.

## Sobre o Projeto
O script principal processa arquivos CSV contendo transcrições de entrevistas com figuras como Donald Trump, Elon Musk, Javier Milei, Mark Cuban e outros. Ele identifica quando duas entidades aparecem próximas no texto e cria uma conexão (aresta) entre elas, permitindo visualizar a estrutura do discurso e as conexões de temas.

## Funcionalidades
* **Extração de Entidades (NER):** Utiliza a biblioteca `spaCy` (modelo en_core_web_md) para identificar entidades relevantes nos textos.
* **Segmentação Adaptativa:** Processamento flexível por sentenças ou janelas de texto (k-caracteres), permitindo diferentes níveis de granularidade na análise.
* **Integração com GitHub:** O notebook pode carregar automaticamente os arquivos CSV diretamente do repositório para execução no Colab.
* **Geração de Grafos:** Exportação de arquivos `.gexf` prontos para visualização e análise de redes no **Gephi**.

## Estrutura do Repositório
* `data/`: Contém as transcrições originais em formato `.csv`.
* `notebooks/`: Notebook principal para execução no Google Colab.
* `output/`: Arquivos de grafos gerados para análise.

## Tecnologias Utilizadas
* **Python 3.12+**
* **Pandas:** Manipulação de dados.
* **spaCy:** Processamento de Linguagem Natural.
* **NetworkX:** Construção e manipulação de estruturas de grafos.
* **RegEx:** Segmentação de texto avançada.

## Como Executar
1. Abra o notebook no Google Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OtavioAntonio/DCA3702_analise-ner-videocasts/blob/main/notebooks/analise_ner.ipynb)

2. Certifique-se de configurar as variáveis no início do código:
   - `COLUNA_TEXTO`: Escolha o número da coluna que está o texto a ser analisado.
   - `MODO_SEGMENTACAO`: Escolha entre `sentenca`, ~~`paragrafo`~~ ou `k-caracteres`, para variar o modo de análise.
   - `CATEGORIAS_ALVO`: Escolha as relações que serão alvo da pesquisa `['PERSON', "ORG", "GPE"]`. Nesse caso será analisado a relação entre pessoas, organizações e países.
   - `MIN_PESO_GEPHI`: Escolha o valor minimo de relações que devem aparecer nos textos para que o valor seja apresentado no resultado final (Grafo).
   - `K_VALOR`: Escolha o total de caracteres a serem analisados no modo `k-caracteres`.

3. Execute a célula para processar os arquivos da pasta `/data` e gerar o arquivo de grafo final.

## Visualização
Após a execução, o arquivo `grafo_segmentacao.gexf` será gerado. 

Para visualizar:
1. Baixe o arquivo gerado na pasta `Arquivos` do Google Colab.
2. Abra no [Gephi](https://gephi.org/).

## Licença
O projeto foi desenvolvido como parte da disciplina **DCA3702 - Algoritmos e Estrutura de Dados II**
