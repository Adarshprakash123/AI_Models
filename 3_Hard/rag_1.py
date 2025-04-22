from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent / "HackerRank Technical Writer Intern – Assessment.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs = text_splitter.split_documents(documents=docs)

embedder = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key="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"
)

vector_store = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

vector_store.add_documents(documents=split_docs)
print("Injection Done")

# vector_store.add_documents(documents=split_docs)
print("Injection Done")

retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

search_result = retriver.similarity_search(
    query="What is ai"
)

print("Relevant Chunks", search_result)