FROM python:3.11

WORKDIR /app

COPY llm-service/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY llm-service /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
