# 🩺 Predição Inteligente de Níveis de Obesidade com Machine Learning

## 📖 Visão Geral

A obesidade é uma das condições de saúde que mais cresce no mundo e está diretamente associada ao aumento do risco de doenças cardiovasculares, diabetes tipo 2 e outras complicações metabólicas.

Com o avanço da Ciência de Dados e da Inteligência Artificial, torna-se possível utilizar informações clínicas e comportamentais para identificar padrões capazes de auxiliar profissionais da saúde na avaliação do estado nutricional dos pacientes.

Este projeto apresenta uma solução baseada em Machine Learning para classificação automática dos níveis de obesidade, transformando dados em informações relevantes para apoio à tomada de decisão.

---

## 🎯 Objetivo do Projeto

Desenvolver um modelo preditivo capaz de identificar o nível de obesidade de um indivíduo a partir de características relacionadas ao seu perfil físico, hábitos de vida e histórico familiar.

Além da modelagem preditiva, o projeto contempla:

* Análise exploratória dos dados;
* Engenharia de atributos;
* Construção de dashboard analítico;
* Aplicação web para predições em tempo real;
* Interpretação dos principais fatores associados à obesidade.

---

## 📂 Conjunto de Dados

A base utilizada reúne informações relacionadas ao estilo de vida e às características físicas dos indivíduos.

### Principais Variáveis

* Idade
* Peso
* Altura
* Consumo diário de água
* Frequência de atividade física
* Histórico familiar de sobrepeso
* Hábitos alimentares
* Tempo de utilização de dispositivos eletrônicos
* Consumo de alimentos altamente calóricos

Como parte do processo de enriquecimento dos dados, foi criado o indicador de Índice de Massa Corporal (IMC), amplamente utilizado na avaliação do estado nutricional.

---

## ⚙️ Processo de Desenvolvimento

### Preparação dos Dados

Durante a etapa de pré-processamento foram realizadas diversas transformações para garantir maior qualidade dos dados:

* Padronização dos atributos;
* Conversão de variáveis categóricas;
* Tratamento de variáveis ordinais;
* Tradução dos campos para português;
* Criação da variável IMC;
* Organização do conjunto para modelagem.

### Modelagem Preditiva

Para o treinamento do modelo foram aplicadas técnicas de Machine Learning utilizando um pipeline automatizado de preparação e classificação.

Etapas executadas:

1. Separação dos dados em treino e teste;
2. Transformação dos atributos através de ColumnTransformer;
3. Treinamento do algoritmo Random Forest;
4. Avaliação por métricas de classificação;
5. Análise da importância das variáveis.

---

## 📈 Desempenho do Modelo

Os resultados obtidos demonstraram excelente capacidade preditiva.

### Principais Indicadores

* Accuracy superior a 98%
* Elevado F1-Score entre as classes
* Baixa taxa de erro de classificação
* Consistência estatística entre treino e teste

A análise das variáveis evidenciou que o IMC é um dos fatores mais relevantes para a determinação do nível de obesidade.

---

## 📊 Business Intelligence e Visualização

Foi desenvolvido um dashboard interativo para apoiar análises e gerar insights sobre o comportamento dos indivíduos presentes na base de dados.

### Dashboard

🔗 Link do Dashboard



### Informações Disponíveis

* Distribuição dos níveis de obesidade;
* Comparação entre grupos populacionais;
* Impacto da atividade física;
* Influência do histórico familiar;
* Indicadores de comportamento alimentar;
* Métricas relacionadas ao IMC.

---

## 🌐 Aplicação Web

A solução foi disponibilizada através de uma interface interativa desenvolvida com Streamlit.

### Acesso



### Recursos Disponíveis

* Cadastro das características do paciente;
* Cálculo automático do IMC;
* Predição instantânea do nível de obesidade;
* Probabilidade associada à classificação;
* Apoio à interpretação dos resultados.

---

## 🏗️ Arquitetura do Projeto

```text
APPOBESIDADE/
│
├── data/
│   └── Obesity.csv
│
├── models/
│   └── obesity_model.pkl
│
├── notebooks/
│   └── TrabalhoPosTechFase4.ipynb
│
├── dashboard/
│   ├── dashboard_obesidade.xlsx
│   └── dashboard_obesidade_paralooker.xlsx
│
├── src/
│   └── train_modelo.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Looker Studio
* Matplotlib
* Seaborn

---

## 🎓 Considerações Finais

Os resultados demonstram que técnicas de Machine Learning podem contribuir significativamente para a identificação precoce de padrões relacionados à obesidade.

A integração entre análise de dados, inteligência artificial e visualização de informações permitiu construir uma solução completa, capaz de transformar dados em conhecimento útil para profissionais da área da saúde e pesquisadores.

Este projeto evidencia como abordagens orientadas por dados podem apoiar decisões mais assertivas e contribuir para iniciativas de prevenção e promoção da saúde.
