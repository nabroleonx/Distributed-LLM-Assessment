from sqlalchemy import Column, DateTime, Integer, String, func

from .database import Base


class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(String, index=True)
    user_input = Column(String)
    response = Column(String)
    timestamp = Column(DateTime, server_default=func.now())
