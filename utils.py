import os
import zipfile
import tempfile
from pathlib import Path
import pandas as pd
from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from langchain_core.documents import Document

def extract_zip(uploaded_file):
    """Extrai arquivos de um .zip para uma pasta temporária."""
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
        zip_ref.extractall(temp_dir)
    return temp_dir

def load_documents_from_folder(folder_path):
    """Carrega conteúdo textual de arquivos suportados em uma pasta."""
    all_text = ""

    for file_path in Path(folder_path).rglob("*"):
        suffix = file_path.suffix.lower()

        try:
            if suffix == ".txt":
                loader = TextLoader(str(file_path), encoding="utf-8")
                docs = loader.load()
                for doc in docs:
                    all_text += doc.page_content + "\n"

            elif suffix == ".pdf":
                loader = PyPDFLoader(str(file_path))
                docs = loader.load()
                for doc in docs:
                    all_text += doc.page_content + "\n"

            elif suffix == ".docx":
                loader = Docx2txtLoader(str(file_path))
                docs = loader.load()
                for doc in docs:
                    all_text += doc.page_content + "\n"

            elif suffix == ".csv":
                df = pd.read_csv(file_path, encoding="utf-8", sep=None, engine="python")
                all_text += df.to_string(index=False) + "\n"

        except Exception as e:
            print(f"[Aviso] Falha ao carregar {file_path.name}: {e}")

    return all_text
