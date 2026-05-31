import streamlit as st
import pandas as pd
import joblib

# --- CONFIGURAÇÃO BÁSICA ---
st.set_page_config(page_title="Sistema Preditivo de Nível de Obesidade", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load("obesity_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")
    model = None

# --- CABEÇALHO ---
st.title("🏥Sistema Preditivo de Nível de Obesidade🏥")
st.markdown("**Alunos:** VICTOR SOARES, CIBELE DE ASSIS, JOSÉ RICARDO, ALEX MOREIRA")
st.divider()

st.subheader("Preencha os dados")

# --- FORMULÁRIO VERTICAL (IDÊNTICO À IMAGEM) ---
gender = st.selectbox("Gênero", ["Male", "Female"])
age = st.number_input("Idade", min_value=10, max_value=100, value=14)
height = st.number_input("Altura (m)", min_value=1.00, max_value=2.50, value=1.00, step=0.01)
weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=30.0, step=0.1)

family_history = st.selectbox("Histórico familiar?", ["yes", "no"])
favc = st.selectbox("Consome alimentos calóricos?", ["yes", "no"])
smoke = st.selectbox("Fuma?", ["yes", "no"])
scc = st.selectbox("Monitora calorias?", ["yes", "no"])

fcvc = st.slider("Consumo vegetais", min_value=1.0, max_value=3.0, value=2.0)
ncp = st.slider("Refeições", min_value=1.0, max_value=4.0, value=3.0)
ch2o = st.slider("Água", min_value=1.0, max_value=3.0, value=2.0)
faf = st.slider("Atividade física", min_value=0.0, max_value=3.0, value=1.0)
tue = st.slider("Uso tecnologia", min_value=0.0, max_value=2.0, value=1.0)

caec = st.selectbox("Come entre refeições?", ["no", "Sometimes", "Frequently", "Always"])
calc = st.selectbox("Consome álcool?", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Transporte", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])

# --- BOTÃO E LÓGICA DE PREDIÇÃO ---
if st.button("Realizar Predição"):
    if model is None:
        st.error("O modelo não foi carregado corretamente.")
    else:
        # 1. Dicionários de mapeamento idênticos ao Jupyter
        map_binario = {"yes": 1, "no": 0}
        map_ordinal = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}

        # 2. Engenharia de Atributos (Cálculo do BMI)
        bmi = weight / (height ** 2)

        # 3. Montando o dicionário na ORDEM EXATA do dataset original
        input_data = {
            "Gender": [gender],
            "Age": [float(age)],
            "Height": [float(height)],
            "Weight": [float(weight)],
            "family_history": [map_binario[family_history]],
            "FAVC": [map_binario[favc]],
            "FCVC": [float(round(fcvc))],
            "NCP": [float(round(ncp))],
            "CAEC": [map_ordinal[caec]],
            "SMOKE": [map_binario[smoke]],
            "CH2O": [float(round(ch2o))],
            "SCC": [map_binario[scc]],
            "FAF": [float(round(faf))],
            "TUE": [float(round(tue))],
            "CALC": [map_ordinal[calc]],
            "MTRANS": [mtrans],
            "BMI": [float(bmi)]
        }

        # Criar DataFrame com as entradas do usuário
        df_input = pd.DataFrame(input_data)

        # --- A MÁGICA COMEÇA AQUI ---
        # Pergunta ao modelo qual foi a exata ordem e os nomes que ele memorizou no treino
        if hasattr(model, 'feature_names_in_'):
            colunas_treino = model.feature_names_in_
            
            # Força o nosso DataFrame a ficar na mesma ordem do modelo
            try:
                df_input = df_input[colunas_treino]
            except KeyError as e:
                st.error(f"❌ ERRO GRAVE DE NOME: O modelo está pedindo uma coluna diferente do que enviamos. Detalhes: {e}")
                st.stop()
        # --- A MÁGICA TERMINA AQUI ---

        # 4. Executando a predição
        try:
            predicao = model.predict(df_input)[0]
            
            st.divider()
            st.subheader("Resultado da Predição")
            st.success(f"**Classificação:** {predicao}")
            st.info(f"**IMC Calculado:** {bmi:.2f}")
            
            # Probabilidade
            try:
                probabilidades = model.predict_proba(df_input)[0]
                max_prob = max(probabilidades) * 100
                st.write(f"**Probabilidade da Predição:** {max_prob:.2f}%")
            except AttributeError:
                pass # Ignora se o modelo não suportar predict_proba
                
        except Exception as e:
            st.error(f"Erro durante a predição: {e}")
