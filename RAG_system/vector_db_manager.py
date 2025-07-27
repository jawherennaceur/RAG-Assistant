from splitter import split_file


def process_new_file(db,file_path):
    docs = split_file(file_path)
    if docs:
        db.add_documents(docs)
        db.persist()


