
from langchain.text_splitter import RecursiveCharacterTextSplitter
from load_files import load_file

def split_file(file_path):
    docs = load_file(file_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    return split_docs