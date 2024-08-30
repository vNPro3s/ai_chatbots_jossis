from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
import os
import glob
import streamlit as st


def process_files(uploaded_files):
    documents = []
    for file in uploaded_files:
        data = file.read()
        file_name = file.name
        with open(file_name, "wb") as f:
            f.write(data)
        if file.type == "application/pdf":
            loader = PyPDFLoader(file_name)
            documents.extend(loader.load())
            print(f"loaded pdf file: {file_name}")
        elif file.type == "text/plain":
            loader = TextLoader(file_name, encoding="utf-8")
            documents.extend(loader.load())
            print(f"loaded text file: {file_name}")
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            loader = Docx2txtLoader(file_name)
            documents.extend(loader.load())
            print(f"loaded docx file: {file_name}")
    return documents

def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", "", " "]
    )
    all_chunks = text_splitter.split_documents(documents)
    return all_chunks


def clear_history():
    if "langchain_messages" in st.session_state:
        del st.session_state["langchain_messages"]

def get_raw_text_from_pdfs():
    # for now fix the folder
    fldr = "C:\REPOS\ML_DP_INTRO\Literature\PDF"
    pdfs = glob.glob(os.path.join(fldr, "*.pdf"))
    print(pdfs)
    pdfs_docs = []

    # get raw text from pdfs
    for pdf in pdfs:
        loader = PyPDFLoader(pdf)
        pdfs_docs.extend(loader.load())

    # concatenate all the documents into one string
    raw_txt = ""
    
    for doc in pdfs_docs:
        content = doc.page_content
        raw_txt += doc.page_content
    
    return raw_txt

# function that makes chunks of text
def get_chunks(raw_txt):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", "", " "]
    )
    chunks = text_splitter.split_text(raw_txt)
    return chunks

# function that performs the vectorization - embeddings and stores them
# into a vectorstore

def get_vectorstore(txt_chunks):
    embeddings = OllamaEmbeddings(model="mistral")
    vectorstore = Chroma.from_documents(txt_chunks, embeddings)
    return vectorstore


if __name__ == "__main__":
    raw = get_raw_text_from_pdfs()
    print(raw)
    chunks = get_chunks(raw)
    print("-"*80)
    print(chunks[0])
    vectorstore = get_vectorstore(chunks)
    print("Finished processing")