from fastmcp import FastMCP, Context
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough

# 1. Create MCP server
mcp = FastMCP("RAG-MCP-Server")

# 2. Load FAISS index
PERSIST_DIR = "faiss_index"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(PERSIST_DIR, embeddings, allow_dangerous_deserialization=True)

# 3. Local LLM via Ollama
llm = ChatOllama(model="llama3.2")

# 4. RAG chain
retriever = RunnableLambda(lambda question: vectorstore.similarity_search(question, k=1))

template = """
Answer all questions in detail, using the context below.
If the question is not answerable, respond with "I don't know".

Question:
{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(template)
])

rag_chain = {
    "context": retriever,
    "question": RunnablePassthrough()
} | prompt | llm

# 5. Define as MCP tool
@mcp.tool(name="ask_faiss")
def ask_faiss(query: str, ctx: Context) -> str:
    ctx.info(f"Received query: {query}")
    result = rag_chain.invoke(query)
    return result.content

# 6. Run the MCP server
if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.2", port=8000, path="/mcp")
