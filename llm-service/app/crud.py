from sqlalchemy import desc
from sqlalchemy.orm import Session

from .models import Conversation


def get_conversations(db: Session, conversation_id: str):
    return (
        db.query(Conversation)
        .filter(Conversation.conversation_id == conversation_id)
        .order_by(desc(Conversation.timestamp))
        .all()
    )


def create_conversation(
    db: Session, conversation_id: str, user_input: str, response: str
):
    db_conversation = Conversation(
        conversation_id=conversation_id, user_input=user_input, response=response
    )
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation
