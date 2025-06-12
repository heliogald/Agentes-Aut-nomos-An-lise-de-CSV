# 🤖 Agente IA com RAG para Análise de CSV (via ZIP)

Este projeto implementa um **Agente de IA baseado em RAG (Retrieval-Augmented Generation)** que permite a **análise de arquivos CSV compactados em um ZIP**, por meio de uma interface amigável com **Streamlit**.

🚀 Totalmente pronto para rodar via **Docker**!

---

## 🧠 O que é RAG?

**Retrieval-Augmented Generation (RAG)** é uma abordagem que combina recuperação de documentos com geração de linguagem natural. Neste projeto, isso permite que a IA leia e compreenda arquivos CSV enviados por você, respondendo a perguntas com base nos dados fornecidos.

---

## 🗂️ Estrutura do Projeto

📦 agente-rag-csv
├── app.py # Interface principal com Streamlit
├── rag_agent.py # Lógica do agente RAG
├── utils/
│ └── extract_zip.py # Extração de arquivos ZIP
├── .streamlit/ # Configurações da interface
├── requirements.txt # Dependências do Python
├── Dockerfile # Dockerfile da aplicação
├── docker-compose.yml # Configuração opcional via Docker Compose
└── README.md # Este arquivo

yaml
Copiar
Editar

---

## ⚙️ Instalação e Execução

### ✅ Pré-requisitos

- [Python 3.10+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

---

### 📦 Execução com Docker

```bash
# Clonar o repositório
git clone https://github.com/heliogald/Agentes-Aut-nomos-An-lise-de-CSV.git
cd Agentes-Aut-nomos-An-lise-de-CSV

# Criar o arquivo .env (ver seção abaixo)

# Construir e executar com Docker
docker build -t agente-rag .
docker run --env-file .env -p 8501:8501 agente-rag
💡 Ou usando Docker Compose
bash
Copiar
Editar
docker-compose --env-file .env up --build
🧪 Executando Localmente (sem Docker)
bash
Copiar
Editar
# Ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Criar o arquivo .env (ver abaixo)

# Inicie a aplicação
streamlit run app.py
🔐 Configuração do .env
Para utilizar o modelo de linguagem (LLM), você precisa fornecer uma chave de API. O projeto está integrado com o provedor OpenRouter.ai, mas você pode usar qualquer provedor compatível com LangChain.

Criar o arquivo .env na raiz do projeto com:
env
Copiar
Editar
OPENROUTER_API_KEY=sua-chave-api-aqui
🔑 Importante: Crie sua chave gratuita ou paga em: https://openrouter.ai/

🧠 Como Usar
Faça upload de um arquivo .zip contendo arquivos .csv.

O agente irá extrair os dados e carregá-los automaticamente.

Digite sua pergunta em linguagem natural.

Receba uma resposta baseada nos dados do CSV.

🛠 Tecnologias Utilizadas
Python

Streamlit – UI interativa

LangChain – Pipeline RAG

Pandas – Manipulação de CSVs

dotenv – Variáveis de ambiente

Docker – Contêiner da aplicação

❓ Suporte
Achou algum bug ou tem sugestões?
📬 Crie uma issue ou entre em contato: helio.galdino@gmail.com

📃 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e distribuir.

Happy Coding! 🚀