from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

from ..crud import create_conversation, get_conversations
from ..database import SessionLocal
from ..schemas import ConversationHistory, Query

router = APIRouter()

model_dict = {
    "llama2": {
        "model": AutoModelForCausalLM.from_pretrained("daryl149/llama-2-7b-chat-hf"),
        "tokenizer": AutoTokenizer.from_pretrained("daryl149/llama-2-7b-chat-hf"),
    },
    "mistral": {
        "model": AutoModelForCausalLM.from_pretrained("Open-Orca/Mistral-7B-OpenOrca"),
        "tokenizer": AutoTokenizer.from_pretrained("Open-Orca/Mistral-7B-OpenOrca"),
    },
}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


template = """
You are a helpful assistant. 

Conversation history:
{context}

Current question:
{question}

Provide a concise response.
"""


@router.post("/query/")
async def query_llm(query: Query, db: Session = Depends(get_db)):
    model_name = query.model
    if model_name not in model_dict:
        raise HTTPException(status_code=400, detail="Invalid model selected")

    model = model_dict[model_name]["model"]

    conversation_id = query.conversation_id or str(len(get_conversations(db, None)) + 1)

    previous_conversations = get_conversations(db, conversation_id)
    context = "\n".join(
        f"{entry.user_input}\n{entry.response}" for entry in previous_conversations
    )

    prompt = template.format(context=context, question=query.question)

    chatbot = pipeline("text-generation", model=model)

    response = chatbot(prompt, max_new_tokens=60)
    generated_text = response[0]["generated_text"].replace(prompt, "").strip()

    create_conversation(db, conversation_id, query.question, generated_text)

    return {"conversation_id": conversation_id, "response": generated_text}


@router.get("/conversation/{conversation_id}", response_model=ConversationHistory)
async def get_conversation(conversation_id: str, db: Session = Depends(get_db)):
    conversation = get_conversations(db, conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    history = [
        {"query": entry.user_input, "response": entry.response}
        for entry in conversation
    ]

    return {
        "conversation_id": conversation_id,
        "history": history,
    }
