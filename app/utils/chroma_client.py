import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from app.config import Config

embedding_fn = SentenceTransformerEmbeddingFunction(
    model_name = Config.MODEL_NAME 
)

client = chromadb.HttpClient(
    host = Config.CHROMA_HOST,
    port = Config.CHROMA_PORT
)

collection = client.get_or_create_collection(
    name = "jarvis",
    embedding_function = embedding_fn
)

def store_chunks(chunks: list[str], source: str, doc_type: str):
    ids = [f"{source}_{i}" for i in range(len(chunks))]
    metadatas = [{
        "source": source,
        "type": doc_type,
        "chunk_index": i
    } for i in range(len(chunks))]

    collection.add(
        ids = ids,
        metadatas=metadatas,
        documents=chunks
    ) 
    print(f"Stored {len(chunks)} chunks into chromadb")