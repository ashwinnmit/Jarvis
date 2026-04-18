from dotenv import load_dotenv
import os
from neo4j import GraphDatabase
import chromadb


load_dotenv()

def check_neo4j():
    try:
        driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
        )
        driver.verify_connectivity()
        driver.close()
        print("NEO4J Connected")
    except Exception as e:
        print(f"Neo4J failed: {e}")

def check_chromadb():
    try:
        client = chromadb.HttpClient(
            host = os.getenv("CHROMA_HOST"),
            port = int(os.getenv("CHROMA_PORT"))
        )
        client.heartbeat()
        print("Chromadb connected")
    except Exception as e:
        print(f"Chromadb failed: {e}")


if __name__ == "__main__":
    print(f"Jarvis Healthchecks")
    check_neo4j()
    check_chromadb()