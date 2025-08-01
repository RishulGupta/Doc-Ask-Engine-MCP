from flask import Flask, request, render_template
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
import os

app = Flask(__name__)

# 1. Load FAISS index
PERSIST_DIR = "faiss_index"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(PERSIST_DIR, embeddings, allow_dangerous_deserialization=True)

# 2. Use Ollama LLM (running locally)
llm = ChatOllama(model="llama3.2")

# 3. Retriever
retriever = RunnableLambda(lambda question: vectorstore.similarity_search(question, k=1))

# 4. Prompt Template
message = """
Answer all questions in detail,
If the question is not answerable say "I don't know".

Question:
{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(message)
])

# 5. RAG Chain
rag_chain = {
    "context": retriever,
    "question": RunnablePassthrough()
} | prompt | llm

# 6. Routes
@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["query"]
        result = rag_chain.invoke(question)
        answer = result.content
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
