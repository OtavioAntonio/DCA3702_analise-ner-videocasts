# Análise de Videocasts: Extração de Entidades e Redes de Coocorrência

Este projeto utiliza Processamento de Linguagem Natural (NLP) para processar transcrições de videocasts (como o Lex Fridman Podcast) e mapear as relações entre as entidades mencionadas (Pessoas, Organizações e Locais). O objetivo final é gerar um grafo de rede que possa ser analisado em ferramentas como o Gephi.

## Sobre o Projeto
O script principal processa arquivos CSV contendo transcrições de entrevistas com figuras como Donald Trump, Elon Musk, Javier Milei, Mark Cuban e outros. Ele identifica quando duas entidades aparecem próximas no texto e cria uma conexão (aresta) entre elas, permitindo visualizar a estrutura do discurso e as conexões de temas.

## Principais Tecnologias

- Python 3.12+
- spaCy: Extração de Entidades Nomeadas (NER) usando o modelo pt_core_news_lg.
- NetworkX: Construção e manipulação do grafo de rede.
- Pandas: Manipulação e limpeza de dados das transcrições.

## Estrutura do Repositório
Seguindo as boas práticas de organização, o projeto está dividido assim:

```text
projeto-videocasts/
├── data/
│   ├── raw/                # Ficheiros .csv originais
│   └── processed/          # Ficheiro .gdf gerado
├── src/
│   └── main.py             # Código principal
├── .gitignore              # Ficheiros ignorados pelo Git
├── README.md               # Documentação
└── requirements.txt        # Dependências do projeto
```

## Como Executar

### Preparação do Ambiente
Clone o repositório e instale as dependências:

### Instalar bibliotecas
pip install -r requirements.txt

### Baixar o modelo de linguagem do spaCy
python -m spacy download pt_core_news_lg

### Configuração de Dados
Coloque as suas transcrições em formato .csv dentro da pasta data/raw/. O script está configurado para ler arquivos com os IDs das entrevistas (ex: qCbfTN-caFI.csv).

### Execução
No script main.py, você pode ajustar o Modo de Segmentação:

sentenca: Analisa conexões dentro da mesma frase.

~~paragrafo: Analisa conexões dentro do mesmo bloco de texto.~~

k-caracteres: Analisa conexões em janelas móveis de texto (ex: a cada 250 caracteres).

Peso Mínimo: Definido para ignorar conexões raras, garantindo que o grafo mostre apenas as relações mais fortes (ex: entidades que aparecem juntas pelo menos 3 vezes).

Categorias Alvo: O projeto foca em PERSON (Pessoas), ORG (Organizações) e GPE (Países/Cidades).

### Execute com:

Bash
python src/main.py

## Resultados e Visualização
Após a execução, um arquivo chamado grafo_entidades.gdf será gerado na pasta data/processed/.

### Como visualizar no Gephi:
Abra o Gephi.

Vá em Arquivo > Abrir e selecione o arquivo .gdf.

No painel "Laboratório de Dados", você verá os nós (entidades) e as arestas (conexões).

Aplique algoritmos de layout como Force Atlas 2 ou Fruchterman Reingold para visualizar a rede.

## Licença
Este projeto foi desenvolvido para fins acadêmicos na disciplina de Inteligência Artificial.