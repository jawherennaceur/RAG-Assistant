from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever,create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import logging
from RAG_system.retriever import retriever
from utils.models import model, contextualize_model
from utils.prompts_templates import system_prompt, contextualize_q_prompt
from utils.conversation_repo import ConversationRepo
from utils.database import get_connection




conn = get_connection()
repo = ConversationRepo(conn)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatRAGAgent:    

    def _get_retriever(self):
        db_path = "RAG_system\db\chroma_docs"
        return retriever.get_retriever(db_path)
        
        
    
    
    def _build_langchain_history(self, messages):
        from langchain_core.messages import HumanMessage, AIMessage
        langchain_messages = []
        for msg in messages:
            if msg["role"] == 'user':
                langchain_messages.append(HumanMessage(content=msg["message"]))
            else:
                langchain_messages.append(AIMessage(content=msg["message"]))
        
        return langchain_messages
    
    def _create_chains(self):

        
        doc_retriever = self._get_retriever()
        
        history_aware_retriever = create_history_aware_retriever(
            contextualize_model, doc_retriever, contextualize_q_prompt
        )        
        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])
        
        question_answer_chain = create_stuff_documents_chain(model, qa_prompt)
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        
        return rag_chain
    
    async def process_message(self, user_id: str,question) -> str:
        try:
            if not question or not question.strip():
                return "Please ask a clear question so I can assist you."

            messages = repo.get(user_id) 
            chat_history = self._build_langchain_history(messages)
        
            rag_chain = self._create_chains()
           
            result = rag_chain.invoke({
                "input": question,
                "chat_history": chat_history,
            }, return_only_outputs=False)
            answer = result.get("answer", "Sorry, I could not answer your question.")
            messages.extend([{"role":"user","message":question},{"role":"assistant","message":answer}])
            repo.upsert(user_id,messages)
            return answer
            
        except Exception as e:
            logger.error(f"Error processing question: {str(e)}")
            return "Sorry, an error occurred while processing your question. Please try again."
    




assistant = ChatRAGAgent()

async def handle_chat_request(user_id:  str,  message: str) -> str:
    return await assistant.process_message(
        user_id=user_id,
        question=message,
    )