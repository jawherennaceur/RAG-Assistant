# RAG Chatbot with Contextualization, Memory, and Vector Database

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot using Langchain, a vector database (Chroma), and a PostgreSQL database for conversation memory. It leverages document embeddings and a contextualizing model to provide accurate, context-aware answers.

### Key Features (Expanded)

- **Retrieval-Augmented Generation (RAG):**  
  The chatbot combines language generation with retrieval of relevant documents.  
  When you ask a question, it searches the vector database for top related documents.  
  Then it generates an answer grounded in those documents, reducing hallucination and increasing accuracy.

- **Contextualization of User Queries:**  
  The system reformulates questions based on the full chat history.  
  This means it understands follow-up questions or ambiguous references without needing the user to repeat context.  
  It produces standalone questions for the retriever to search more effectively.

- **Vector Database Using Chroma:**  
  Documents are split into small chunks for better embedding granularity.  
  Each chunk is converted into a numerical vector using a HuggingFace embedding model.  
  These vectors are stored in Chroma for fast semantic similarity search.  
  This allows retrieving documents that match the question’s meaning, not just keywords.

- **Conversation Memory with PostgreSQL:**  
  User conversations are saved as JSON in a PostgreSQL database.  
  This allows tracking conversation history per user to provide context in multi-turn dialogue.  
  It helps the chatbot maintain personalized and coherent interactions over time.

- **File Processing Pipeline:**  
  Supports loading `.pdf` and `.docx` files.  
  Files are split into manageable chunks using text splitters to improve retrieval precision.  
  Chunks are embedded and stored in the vector database automatically.

- **FastAPI Endpoint:**  
  Provides an HTTP API for sending chat requests asynchronously.  
  Supports multiple users via user IDs, preserving separate conversation histories.

---

## Setup Instructions

### 1. Environment Variables

Create a `.env` file with:

```
GOOGLE_API_KEY=your_google_api_key
HuggingFace_KEY=your_huggingface_api_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

### 2. Database Setup

Set up a PostgreSQL database with a table `conversations`:

```sql
CREATE TABLE conversations (
    user_id TEXT PRIMARY KEY,
    messages JSONB NOT NULL
);
```

This table stores user conversation messages in JSON format.

### 3. Document Storage

- Place documents (`.pdf`, `.docx`) in the `data` folder.
- Run your ingestion script to load, split, embed, and store them in the Chroma vector DB (`db/chroma_docs`).

### 4. Running the API

Start the FastAPI server:

```bash
uvicorn main:app --port 7000
```

Access the health check endpoint:

```
GET /health
Response: {"status":"ok"}
```

### 5. Using the Chatbot

Send POST requests to `/ask` with JSON payload:

```json
{
  "user_id": "unique_user_id",
  "message": "Your question here"
}
```

The API returns:

```json
{
  "answer": "The chatbot's response based on documents and conversation context."
}
```

---

## Prompt Customization

The system prompt controls how the assistant answers:

```python
system_prompt = """
You are a helpful AI assistant.  
Use the information from the provided documents and the previous conversation to answer the user’s question clearly and precisely.  
If the answer is not found in the documents, respond: "I do not have enough information to answer that."  
Keep your response brief and focused on the user’s question.

Documents:
{documents}
"""
```

To adjust behavior:

- Modify instructions to the assistant.
- Add or remove information in the prompt.
- Use `{documents}` placeholder to inject retrieved documents text dynamically.
- Ensure your chain passes retrieved documents as a formatted string to the prompt input.

---

## Notes

- The vector database is stored persistently in `db/chroma_docs`.
- Conversation history allows multi-turn dialogue and improves contextual understanding.
- You can extend the file loader to support more file types.
- Ensure environment variables are set correctly for API keys and database access.
