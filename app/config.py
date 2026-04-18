from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Neo4J
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    # chroma
    CHROMA_HOST = os.getenv("CHROMA_HOST")
    CHROMA_PORT = os.getenv("CHROMA_PORT")

    #LLM
    MODEL_NAME = "all-MiniLM-L6-v2"

    #paths
    WATCH_FOLDER = os.path.abspath("data/watch")