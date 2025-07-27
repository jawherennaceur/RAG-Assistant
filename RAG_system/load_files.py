from langchain.document_loaders import PyMuPDFLoader, UnstructuredWordDocumentLoader


def load_file(file_path):
    if file_path.endswith(".pdf"):
        loader = PyMuPDFLoader(file_path)
        docs = loader.load()
    elif file_path.endswith(".docx") or file_path.endswith(".doc"):
        loader = UnstructuredWordDocumentLoader(file_path)
        docs = loader.load()
    else:
        docs = []
    return docs 
