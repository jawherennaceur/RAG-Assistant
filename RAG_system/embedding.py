from langchain_huggingface import HuggingFaceEmbeddings
from huggingface_hub import login
from config import HuggingFace_KEY
login(HuggingFace_KEY)

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
