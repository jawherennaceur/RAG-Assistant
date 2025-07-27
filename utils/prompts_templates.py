from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
system_prompt = """
You are a helpful AI assistant.  
Use the information from the provided documents and the previous conversation to answer the user’s question clearly and precisely.  
If the answer is not found in the documents, respond: "I do not have enough information to answer that."  
Keep your response brief and focused on the user’s question.
Documents:
{documents}
"""




contextualize_q_system_prompt = """
Given a chat history and the latest user question which might reference context in the chat history, 
formulate a standalone question which can be understood without the chat history. 
Do NOT answer the question, just reformulate it if needed and otherwise return it as is.
"""


contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])