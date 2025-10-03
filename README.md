# Eleven Madison Park - AI Q&A Assistant 💬  

An **AI-powered Retrieval-Augmented Generation (RAG) application** that allows users to ask natural language questions about **Eleven Madison Park Restaurant** based on its text data (e.g., menu, history, philosophy).  
The app leverages **LangChain**, **Ollama (Gemma3 LLM + Nomic embeddings)**, **ChromaDB**, and **Gradio** to provide accurate, source-backed answers.  

---

## 🚀 Features
- 📂 Load documents from a text file (`eleven_madison_park_data.txt`).  
- ✂️ Split documents into overlapping chunks for better retrieval.  
- 🔎 Store and search chunks using **ChromaDB** vector store with **Nomic embeddings**.  
- 🤖 Use **Ollama’s Gemma3:1b** model for question-answering.  
- 📜 Return answers **with cited sources**.  
- 🎨 User-friendly **Gradio web interface**.  
- 🧩 Plug-and-play architecture (easy to swap embeddings/LLM/vector store).  

---

## 🛠️ Tech Stack
- **Python 3.10+**
- [LangChain](https://python.langchain.com) – Orchestration
- [Ollama](https://ollama.ai) – Local LLM & Embeddings
- [ChromaDB](https://www.trychroma.com) – Vector Store
- [Gradio](https://gradio.app) – Web UI

---

## 📂 Project Structure
```
📦 eleven-madison-assistant
├── eleven_madison_park_data.txt     # Source data file
├── main.py                          # Entry point
├── chunking.py                      # Splits docs into chunks
├── embeddings_and_vector_store.py   # Embeddings + ChromaDB
├── rag_chain.py                     # RAG chain definition
├── infrance.py                      # Query processing logic
├── gradio_interface.py              # UI setup
└── README.md                        # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/IsmailMohamed010/eleven_madison_park_data_RAG.git
cd eleven_madison_park_data_RAG
```

2. **Set up Python environment**
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install & run Ollama**  
Follow the [Ollama installation guide](https://ollama.ai/download).  
Make sure you have pulled required models:
```bash
ollama pull gemma3:1b
ollama pull nomic-embed-text
```

---

## ▶️ Running the App

1. Place your dataset into the root folder as `eleven_madison_park_data.txt`.  
   (Replace with your own restaurant/business text if needed.)  

2. Run the main script:
```bash
python main.py
```

3. Open the Gradio UI link in your browser (usually `http://127.0.0.1:7860`).  

---

## 💡 Example Queries
- *"What are the different menu options and prices?"*  
- *"Who is the head chef?"*  
- *"What is Magic Farms?"*  
- *"Is Eleven Madison Park plant-based?"*  

---

## 📌 Notes
- If `vector store creation resulted in 0 items`, check that your data file is non-empty and encoded in **UTF-8**.  
- Ollama must be running in the background before launching the app.  
- Adjust chunk size/overlap in `chunking.py` if answers seem incomplete.  
