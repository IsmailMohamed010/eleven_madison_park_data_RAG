from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.llms import Ollama

def rag_chain(vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    print("Retriever configured successfully from vector store.")

    # --- 2. Define the Language Model (LLM) from Ollama ---
    llm = Ollama(model="gemma3:1b", temperature=0)
    print("Gemma LLM successfully initialized.")

    # --- 3. Create the RetrievalQAWithSourcesChain ---
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        verbose=True
    )
    print("RetrievalQAWithSourcesChain created successfully.")

    return qa_chain