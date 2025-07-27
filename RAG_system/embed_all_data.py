import os
from vector_db_manager import process_new_file
from langchain_community.vectorstores import Chroma
from embedding import embedding




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = (os.path.dirname(BASE_DIR))
DB_DIR = os.path.join(BASE_DIR,'db')
DATA_FOLDER = os.path.join(BASE_DIR,'data')


data_folder = os.path.join(BASE_DIR, 'data')

for root, dirs, files in os.walk(data_folder):
    if files != []:
        store_name = f"chroma_docs"
        persist_dir = os.path.join(DB_DIR, store_name)
        db = Chroma(persist_directory=persist_dir, embedding_function=embedding)
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                process_new_file(db, file_path)

