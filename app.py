import streamlit as st
from utils import extract_zip
from dotenv import load_dotenv
import os
import pandas as pd

# 📌 Configuração da página (deve ser a primeira instrução do script)
st.set_page_config(page_title="RAG com ZIP", layout="centered")

# ✅ Carregar variáveis do .env (como OPENROUTER_API_KEY)
load_dotenv()

st.title("📦 Agente IA com RAG (CSV ZIP)")

uploaded_file = st.file_uploader(
    "📁 Faça upload de um arquivo .zip contendo os arquivos CSV fornecidos", type="zip"
)

if uploaded_file:
    try:
        with st.spinner("⏳ Extraindo e carregando os dados dos arquivos CSV..."):
            extracted_path = extract_zip(uploaded_file)
            
            # ✅ Carregando DataFrame diretamente
            df_list = []
            for filename in os.listdir(extracted_path):
                if filename.endswith(".csv"):
                    df_list.append(pd.read_csv(os.path.join(extracted_path, filename), encoding="utf-8"))

            if not df_list:
                raise ValueError("Nenhum arquivo CSV encontrado no ZIP.")

            df = pd.concat(df_list, ignore_index=True)

            st.success("✅ Dados carregados! Faça sua pergunta abaixo.")

            # ✅ Criar campo de entrada com chave para controlar estado
            query = st.text_input("❓ Digite sua pergunta sobre os dados:", key="query_input")

            # ✅ Resetar resposta ao modificar o campo de entrada
            if query == "":
                st.session_state.pop("last_response", None)

            if query:
                with st.spinner("🤖 Analisando..."):
                    from rag_agent import create_df_agent  
                    agent = create_df_agent(extracted_path)  
                    result = agent.invoke({"input": query})  
                    st.session_state["last_response"] = result  # Atualiza estado com resposta da IA

            # ✅ Exibe a resposta armazenada no estado
            if "last_response" in st.session_state and st.session_state["last_response"]:
                st.markdown(f"**💬 Resposta:** {st.session_state['last_response']}")

    except Exception as e:
        st.error(f"❌ Ocorreu um erro ao processar os documentos:\n`{str(e)}`")
