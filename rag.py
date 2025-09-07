from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from settings import CHROMA_PERSIST_DIR

# splitter and embeddings
splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=200)

def build_index(docs: list[dict], persist_dir: str = CHROMA_PERSIST_DIR, embedding_model: str = "models/embedding-001"):
    """
    docs: list of {"url":..., "text": "..."}
    returns: a Chroma vectorstore persisted to persist_dir
    """
    texts = []
    metadatas = []
    for d in docs:
        chunks = splitter.split_text(d["text"])
        for c in chunks:
            texts.append(c)
            metadatas.append({"source": d["url"]})

    embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model,   # ensure key is picked up
        transport="rest")  # uses GOOGLE_API_KEY
    vectordb = Chroma.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas, persist_directory=persist_dir)
    return vectordb

def get_retriever(vectordb, k: int = 6):
    return vectordb.as_retriever(search_kwargs={"k": k})
