## 🗨️**Doc Ask Engine MCP**

A customizable, agent-powered GenAI chatbot for querying your own documents and data — originally built for **Naukri.com** to automate HR policy queries.

---

## 🔍 What is Doc Ask Engine MCP?

**Doc Ask Engine MCP** is an AI-powered question-answering engine that lets you "talk" to your internal documents. It uses **Generative AI** and **agentic reasoning**, hosted on an **MCP (Modular Command Processing) server**, to return intelligent answers to user queries based on custom data.

Originally developed during my internship at **Naukri.com**, it helped answer questions like:

- 🕒 *What are the office timings?*
- 📝 *How many leaves can I take in a year?*
- 💰 *What’s the reimbursement process?*

Now open-sourced and **fully customizable** — plug in **your own PDFs** to build a Q&A engine for *any* domain (HR, legal, medical, etc.).

---

## ⚡ Features

✅ GenAI + Agentic reasoning  
📄 PDF-based ingestion  
🧠 FAISS-powered similarity search  
🖥️ API served via MCP Server  
🔄 Fully customizable with your data  

---

## 🚀 Getting Started

### 🧾 Step 1: Clone the Repository

```bash
git clone https://github.com/RishulGupta/Doc-Ask-Engine-MCP.git
cd Doc-Ask-Engine-MCP
```

---

### 📁 Step 2: Add Your PDFs

Create a folder and add your documents:

```
Doc-Ask-Engine-MCP/
└── my_data/
    ├── handbook.pdf
    └── code_of_conduct.pdf
```

---

### ⚙️ Step 3: Modify `data_ingestion.py`

Edit the file and change this line:

```python
SOURCE_DIRECTORY = "my_data"
```

Then run:

```bash
python data_ingestion.py
```

This generates a FAISS index from your documents.

---

### 🧠 Step 4: Start the MCP Server

```bash
python mainwithmcp.py
```

You’ll see the server starting up.

---

### 🗨️ Step 5: Ask Questions

📡 **Endpoint:** `http://127.0.0.2:8000/mcp/ask_faiss`

Send a POST request with:

```json
{
  "ask_query": "What are the office working hours?"
}
```

You'll get a smart AI-generated response based on your uploaded documents.

---

## 🧩 How It Works

1. 📚 Parse and chunk PDFs  
2. ✨ Embed text using GenAI  
3. 🧭 Store embeddings with FAISS  
4. 🔎 Retrieve relevant chunks  
5. 🤖 Agent synthesizes final answer  
6. 🌐 Answer served via MCP endpoint

---

## 👨‍💻 Author

**Rishul Gupta**  

---

## 📌 Notes
- 🔓 Built for Naukri, generalized for everyone
---

