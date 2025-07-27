from fastapi import APIRouter, HTTPException
import traceback
from services.ChatBot import handle_chat_request

from pydantic import BaseModel



class AskRequest(BaseModel):
    user_id: str
    message: str

router = APIRouter()
@router.post("/ask")
async def ask_question(req: AskRequest):
    try:
        response = handle_chat_request(req.user_id,req.message)
        return {"answer": response}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
