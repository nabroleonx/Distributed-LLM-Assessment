from typing import List, Optional

from pydantic import BaseModel


class Query(BaseModel):
    model: str
    query: str
    conversation_id: Optional[str] = None

class ConversationBase(BaseModel):
    query: str
    response: str

class ConversationHistory(BaseModel):
    conversation_id: str
    history: List[ConversationBase]
