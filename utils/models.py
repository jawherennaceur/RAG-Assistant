from config import GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.2)

contextualize_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0)


