from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(raw_documents: str, chunk_size: int, chunk_overlap: int):
    """Splits text into chunks of specified size with overlap."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,  # Aim for chunks of about 1000 characters
                                               chunk_overlap = 150,)  # Each chunk overlaps with the previous by 150 characters

    # Split the raw document(s) into smaller Document objects (chunks)
    documents = text_splitter.split_documents(raw_documents)

    # Check if splitting produced any documents
    if not documents:
        raise ValueError("Error: Splitting resulted in zero documents. Check the input file and splitter settings.")
    print(f"Document split into {len(documents)} chunks.")
    return documents
