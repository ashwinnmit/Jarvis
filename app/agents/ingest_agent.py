import os
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from app.extractors import extract_text, extract_pdf
from app.utils.chunker import chunk_text
from app.utils.chroma_client import store_chunks
from app.config import Config


class IngestHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return 
        
        filepath = event.src_path
        filename = os.path.basename(filepath)
        ext = os.path.splitext(filepath)[-1].lower()

        print(f"Detected: {filename}")
        time.sleep(1)

        try:
            if ext == ".pdf":
                text = extract_pdf(filepath)
                doc_type = "pdf"
            elif ext in [".txt", ".md"]:
                content = extract_text(filepath)
                text = content 
                doc_type = ext.replace(".", "")
            else:
                print(f"Unsupported file format: {ext}, skipping")
                return 
            
            if not text:
                print(f"No text is extracted from {filepath}, skipping")
                return 
            
            print(f"Extracted {len(text)} characters")

            chunks = chunk_text(text)
            print(f"Split into {len(chunks)} chunks of text")

            store_chunks(chunks, source = filename, doc_type=doc_type)
        except Exception as e:
            print(f"Failed to ingest {filepath}, {e}")

    
def start_ingest_agent():
    print(f"Watching folder: {Config.WATCH_FOLDER}")

    observer = Observer()
    observer.schedule(IngestHandler(), path=Config.WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(f"Ingest agent stopped")

    observer.join()

if __name__ == "__main__":
    start_ingest_agent()