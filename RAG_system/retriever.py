from langchain_community.vectorstores import Chroma
from .embedding import embedding


class retriever :
    @classmethod
    def get_retriever(cls,persistent_directory):
        db = Chroma(persist_directory=persistent_directory,embedding_function=embedding)
        print(db._collection.count()) 
        retriever = db.as_retriever(search_type="similarity",search_kwargs=    {"k":3})
        return  retriever
         
