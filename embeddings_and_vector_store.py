from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


def embeddings_and_vector_store(documents):

    # Use Ollama with Nomic Embed Text
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    print("Nomic Embed Text model initialized via Ollama.")

    # Create ChromaDB vector store
    print("\nCreating ChromaDB vector store and embedding documents...")

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings
    )

    # Verify count
    vector_count = vector_store._collection.count()
    print(f"ChromaDB vector store created with {vector_count} items.")

    if vector_count == 0:
        raise ValueError("Vector store creation resulted in 0 items. Check previous steps.")
    
    return vector_store