def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Splits text into chunks respecting paragraph boundaries wherever possible. 
    Fallback to word-level chunking

    ToDo:
        -> Maybe implement Recursive character text splitter in the future ?
    """

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) <= chunk_size:
            current_chunk += " " + para
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            if len(para) > chunk_size:
                words = para.split()
                temp = ""
                for word in words:
                    if len(temp) + len(word) <= chunk_size:
                        temp += " " + word
                    else:
                        chunks.append(temp.strip())
                        temp = word
                if temp:
                    current_chunk = temp
            else:
                current_chunk = para

    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks 