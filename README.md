
# 📦 Agente IA com RAG (CSV ZIP)

Este projeto implementa um **Agente IA com RAG** (Retrieval-Augmented Generation) utilizando arquivos CSV compactados em um ZIP. Agora, suportamos **Docker** para facilitar a instalação e execução.

## 🚀 Instalação

### 1. Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

### 2. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 3. Construir e Executar com Docker

```bash
docker build -t agente-rag .
docker run -p 8501:8501 agente-rag
```

### 4. Utilizando docker-compose

```bash
docker-compose up --build
```

## 🏗 Estrutura do Projeto

```
📦 seu-repositorio
├── Dockerfile
├── docker-compose.yml  # (opcional)
├── requirements.txt
├── app.py
├── utils/
├── rag_agent.py
├── README.md
```

## 🌟 Uso da Aplicação

1. Faça upload de um arquivo `.zip` contendo os arquivos `.csv`.
2. Aguarde a extração dos arquivos e o carregamento dos dados.
3. Digite sua pergunta sobre os dados carregados.
4. Receba a resposta da IA baseada nos arquivos CSV enviados!

## 🔧 Tecnologias Utilizadas

- **Docker**: Para empacotamento e execução eficiente da aplicação.
- **Streamlit**: Interface interativa para interagir com os dados.
- **Pandas**: Manipulação de dados CSV.
- **python-dotenv**: Gerenciamento de variáveis de ambiente.
- **LangChain + OpenRouter**: Implementação de IA para análise de dados com RAG.
- **utils.extract_zip**: Função para extração de arquivos ZIP.

## ❓ Suporte

Se encontrar problemas, crie uma issue no repositório ou entre em contato com o desenvolvedor.

---

**Happy coding! 🚀**
