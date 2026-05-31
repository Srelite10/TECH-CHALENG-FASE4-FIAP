# 🩺 Predição Inteligente de Níveis de Obesidade com Machine Learning

## 📖 Visão Geral

A obesidade representa um dos principais desafios de saúde pública da atualidade, estando associada ao aumento da incidência de doenças cardiovasculares, diabetes mellitus tipo 2, hipertensão arterial e outras condições crônicas que impactam significativamente a qualidade de vida da população.

Com o avanço das técnicas de Ciência de Dados e Inteligência Artificial, tornou-se possível utilizar informações biométricas, comportamentais e hereditárias para identificar padrões capazes de auxiliar na compreensão dos fatores relacionados ao desenvolvimento da obesidade.

Este projeto apresenta uma solução completa baseada em Machine Learning para classificação automática dos níveis de obesidade, combinando modelagem preditiva, análise exploratória de dados, Business Intelligence e visualização interativa de informações.

---

## 🎯 Objetivo do Projeto

Desenvolver um modelo preditivo capaz de identificar o nível de obesidade de um indivíduo a partir de características relacionadas ao seu perfil físico, hábitos de vida e histórico familiar.

Além da modelagem preditiva, o projeto contempla:

* Análise exploratória dos dados;
* Tratamento e transformação das variáveis;
* Engenharia de atributos;
* Construção de pipeline automatizada de Machine Learning;
* Desenvolvimento de dashboard analítico;
* Aplicação web para predições em tempo real;
* Interpretação dos principais fatores associados à obesidade.

---

## 📂 Conjunto de Dados

A base utilizada reúne informações relacionadas ao estilo de vida, hábitos alimentares e características físicas dos indivíduos avaliados.

### Principais Variáveis

* Idade
* Peso
* Altura
* Gênero
* Consumo diário de água
* Frequência de atividade física
* Histórico familiar de sobrepeso
* Hábitos alimentares
* Número de refeições diárias
* Tempo de utilização de dispositivos eletrônicos
* Meio de transporte utilizado
* Consumo de alimentos altamente calóricos

Como parte do processo de enriquecimento dos dados, foi criada a variável **Índice de Massa Corporal (IMC)**, amplamente utilizada na literatura médica para avaliação do estado nutricional e classificação dos níveis de obesidade.

---

## ⚙️ Processo de Desenvolvimento

### Preparação dos Dados

Durante a etapa de pré-processamento foram realizadas diversas transformações visando garantir consistência e qualidade ao conjunto de dados:

* Tratamento de variáveis categóricas;
* Conversão de atributos binários;
* Padronização de variáveis numéricas;
* Transformação de variáveis ordinais;
* Tradução dos campos para português;
* Criação da variável derivada IMC;
* Organização dos dados para modelagem.

### Modelagem Preditiva

O processo de modelagem foi estruturado utilizando uma pipeline automatizada desenvolvida com Scikit-Learn.

Etapas executadas:

1. Separação dos dados em conjuntos de treino e teste;
2. Definição dos grupos de variáveis;
3. Aplicação de transformações através do ColumnTransformer;
4. Codificação das variáveis categóricas utilizando One-Hot Encoding;
5. Treinamento do algoritmo Random Forest;
6. Avaliação por métricas de classificação;
7. Interpretação da importância das variáveis.

### Algoritmo Utilizado

O modelo foi desenvolvido utilizando o algoritmo **Random Forest Classifier**, técnica baseada em múltiplas árvores de decisão que combina robustez, interpretabilidade e elevada capacidade de generalização para problemas de classificação multiclasse.

---

## 📈 Desempenho do Modelo

Os resultados obtidos demonstraram excelente capacidade preditiva na classificação dos diferentes níveis de obesidade.

### Principais Indicadores

* Accuracy aproximada de 98,8%;
* Elevado Precision Score entre as classes;
* Alto Recall Score;
* Excelente F1-Score;
* Baixa taxa de erro de classificação;
* Consistência entre treino e teste.

O desempenho alcançado superou amplamente o requisito mínimo estabelecido pelo desafio, demonstrando a eficiência do modelo na identificação dos diferentes perfis de obesidade presentes na base de dados.

---

## 🔍 Principais Descobertas Analíticas

A análise exploratória permitiu identificar fatores relevantes associados aos diferentes níveis de obesidade observados na população estudada.

Entre os principais achados destacam-se:

* O Índice de Massa Corporal (IMC) apresentou a maior relevância preditiva no modelo;
* O peso corporal demonstrou forte influência na classificação dos indivíduos;
* A frequência de atividade física apresentou relação inversa com níveis mais elevados de obesidade;
* O histórico familiar mostrou associação importante com categorias mais severas da condição;
* Variáveis relacionadas aos hábitos alimentares contribuíram significativamente para a diferenciação entre os grupos;
* Fatores comportamentais e hereditários mostraram impacto relevante no processo de classificação.

Esses resultados reforçam a natureza multifatorial da obesidade, evidenciando a influência conjunta de aspectos físicos, comportamentais e genéticos.

---

## 📊 Dashboard Analítico

Com o objetivo de ampliar a capacidade de interpretação dos resultados, foi desenvolvido um dashboard interativo no Looker Studio estruturado em três módulos analíticos.

### 1️⃣ Visão Analítica da Obesidade

Painel destinado à análise geral da população estudada e dos níveis de obesidade observados.

Principais indicadores:

* Distribuição dos níveis de obesidade;
* Comparação por gênero;
* IMC médio por classe;
* Indicadores populacionais;
* Perfil geral dos indivíduos analisados.

### 2️⃣ Análise de Padrões Comportamentais

Painel voltado à investigação dos hábitos associados aos diferentes níveis de obesidade.

Principais análises:

* Frequência de atividade física;
* Consumo médio de água;
* Tempo de utilização de dispositivos eletrônicos;
* Comparação comportamental entre grupos.

### 3️⃣ Análise dos Fatores Genéticos e de Risco Associados à Obesidade

Painel destinado à avaliação dos fatores hereditários e comportamentais relacionados ao desenvolvimento da obesidade.

Principais análises:

* Histórico familiar;
* Consumo de álcool;
* Tabagismo;
* Tempo de tela;
* Indicadores de risco associados.

### Dashboard

🔗 Link do Dashboard

((https://datastudio.google.com/reporting/8cd6c142-1532-4e07-a91c-c282c6a237f3))

---

## 🌐 Aplicação Web

A solução foi disponibilizada através de uma aplicação interativa desenvolvida com Streamlit, permitindo que usuários realizem previsões em tempo real por meio do preenchimento de características pessoais e comportamentais.

### Recursos Disponíveis

* Cadastro das características do indivíduo;
* Cálculo automático do IMC;
* Predição instantânea do nível de obesidade;
* Exibição das probabilidades associadas à classificação;
* Interface amigável para apoio à análise dos resultados.

### Aplicação

🔗 Link da Aplicação

((https://tech-chaleng-fase4-fiap-dzn2kcdkrv9fakotnbp2ph.streamlit.app/))

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
* Joblib

---

## 🎓 Conclusões

O desenvolvimento deste projeto demonstrou a aplicação prática de técnicas de Ciência de Dados, Machine Learning e Business Intelligence na análise de fatores associados à obesidade.

Os resultados evidenciaram a elevada capacidade preditiva do algoritmo Random Forest, alcançando aproximadamente 98,8% de acurácia na classificação dos diferentes níveis de obesidade presentes na base de dados.

Além da modelagem preditiva, a construção de dashboards analíticos possibilitou explorar fatores físicos, comportamentais e hereditários relacionados à condição, ampliando a compreensão dos padrões identificados durante o estudo.

A integração entre análise exploratória, modelagem estatística, visualização de dados e aplicações interativas resultou em uma solução completa, capaz de transformar dados em informações relevantes para análises, pesquisas e suporte à tomada de decisão baseada em evidências.

Este projeto evidencia o potencial da Ciência de Dados como ferramenta para geração de conhecimento e identificação de padrões complexos em problemas relacionados à saúde e ao comportamento humano.
