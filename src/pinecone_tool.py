from langchain.agents import tool
from sentence_transformers import SentenceTransformer
from langchain_pinecone import PineconeVectorStore
import pinecone
from langchain_huggingface import HuggingFaceEmbeddings 
import os
from dotenv import load_dotenv


load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")



os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

#index name

index_name = os.getenv("medical-chatbot2")


#STEP1:EMBEDDING model

EMBEDDING_MODEL =HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#step-2 store from existing pinecone index

doc_search=PineconeVectorStore.from_existing_index(
    
    index_name="medical-chatbot2",
    embedding=EMBEDDING_MODEL
)


#step3 retrieve
retriever = doc_search.as_retriever(search_type="similarity" ,search_kwargs={"k":3})




#step4 
@tool

def search_doc(query:str) -> str:

    """
    Searches for relevant documents from the medical knowledge base using the query.

    """

    document = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in document])