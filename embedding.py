import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient

MONGO_URI = os.environ["MONGO_URI"]

# Konfigurasi Atlas mongodb
DB_NAME = "vectorstores"
COLLECTION_NAME = "medibot"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "default"
EMBEDDING_FIELD_NAME = "embedding"
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
MONGODB_COLLECTION = db[COLLECTION_NAME]

if __name__ == "__main__":
    # Path relatif ke file PDF di direktori data
    pdf_path = os.path.join(os.path.dirname(__file__), "data", "The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf")
    
    # Memuat dokumen
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # membagi dokumen menjadi chunk
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(pages)
    
    # Log jumlah dokumen yang di-split
    print(f"Jumlah dokumen yang di-split: {len(texts)}")

    # ekstrak teks untuk setiap dokumen
    documents_texts = [doc.page_content for doc in texts]

    # Menghasilkan embeddings untuk setiap document
    embeddings = OpenAIEmbeddings(model='text-embedding-3-small', disallowed_special=())
    embedded_texts = embeddings.embed_documents(documents_texts)

    # Memasukkan document ke MongoDB Atlas Vector Search
    vector_search = MongoDBAtlasVectorSearch(
        collection=MONGODB_COLLECTION,
        embedding=embeddings,
    )
    
    # Log hasil embedding dan masukkan ke dalam koleksi
    for i, doc in enumerate(texts):
        print(f"Dokumen {i}: {doc}")
        # Pastikan _id adalah string
        doc_id = str(i)
        vector_search.add_documents(documents=[doc], embeddings=[embedded_texts[i]], ids=[doc_id])
        print(f"Dokumen {i} berhasil dimasukkan ke dalam koleksi dengan embedding.")

    # Log total dokumen yang berhasil dimasukkan
    print(f"Total dokumen yang berhasil dimasukkan: {len(texts)}")
