from langchain.document_loaders import TextLoader
from chunking import chunk_text
from embeddings_and_vector_store import embeddings_and_vector_store
from rag_chain import rag_chain
from infrance import ask_elevenmadison_assistant
from gradio_interface import gradio_interface

def load_documents(file_path):
    """
    Load documents from a text file.
    """
    loader = TextLoader(file_path, encoding = "utf-8")
    documents = loader.load()
    return documents

if __name__ == "__main__":
    file_path = "eleven_madison_park_data.txt"
    documents = load_documents(file_path)
    for doc in documents:
        print(doc.page_content)
    print(f"Total documents loaded: {len(documents)}")
    chunked_text = chunk_text(documents, chunk_size=1000, chunk_overlap=150)
    vector_store = embeddings_and_vector_store(chunked_text)
    qa_chain = rag_chain(vector_store)
    DATA_FILE_PATH = file_path
    ask_elevenmadison_assistant_partial = lambda user_query: ask_elevenmadison_assistant(user_query, qa_chain, DATA_FILE_PATH)
    gradio_interface(ask_elevenmadison_assistant_partial)
