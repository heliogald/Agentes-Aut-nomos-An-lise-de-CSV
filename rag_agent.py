import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# ✅ Criar agente de IA para perguntas fora do escopo
def create_df_agent(folder_path):
    dfs = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path, encoding="utf-8")
            dfs.append(df)

    if not dfs:
        raise ValueError("Nenhum arquivo CSV encontrado na pasta.")

    combined_df = pd.concat(dfs, ignore_index=True)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        max_tokens=1024  # Redução de tokens para evitar erro no modelo mini
    )

    @tool
    def describe_dataframe(query: str) -> str:
        """Usa IA para responder perguntas fora do escopo pré-definido com base em uma amostra do DataFrame."""
        
        # ✅ Enviar apenas uma amostra dos dados, convertidos para dicionário
        dados_amostra = combined_df.head(5).to_dict()

        prompt = f"""
        Você tem acesso a um conjunto de dados representado pelo seguinte exemplo:
        {dados_amostra}

        Responda à seguinte pergunta com base nesses dados: '{query}'
        """

        return llm.invoke(prompt)

    tools = [describe_dataframe]

    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "Você é um assistente que responde perguntas sobre um DataFrame. "
            "Se a pergunta for sobre 'fornecedor, item, notas fiscais em janeiro ou valor médio', responda diretamente. "
            "Caso contrário, use IA para gerar uma resposta baseada nos dados."
        ),
        HumanMessagePromptTemplate.from_template("{input}\n\n{agent_scratchpad}")
    ])

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True, output_key="output")

    return executor
