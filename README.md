# LLM Service using FastAPI

The FastAPI server provides endpoints to interact with a language model, maintaining conversation history and allowing users to query the model.

## Setup Instructions

- Clone the Repository

  ```
  git clone https://github.com/nabroleonx/Distributed-LLM-Assessment.git .
  cd /llm-service
  ```

- Create a virtual environment and activate it

  ```
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  ```

- Install Dependencies

  ```
  pip install -r requirements.txt
  ```

- Run the FastAPI Server

  ```
  uvicorn app.main:app --host 0.0.0.0 --port 8000
  ```

# Consumer API using Node.js

The Node.js server acts as a middle layer, sending user queries to the FastAPI server and managing conversation histories.

## Setup Instructions

- Clone the Repository

  ```
  git clone https://github.com/nabroleonx/Distributed-LLM-Assessment.git .
  cd /consumer-api
  ```

- Install Dependencies

  ```
  pnpm install
  ```

- Run the Node.js Server

  ```
  pnpm start
  ```

## Docker Setup

If you prefer using Docker, follow these steps:

- Build and Run the Docker Image

  ```
  make up
  ```

  This setup ensures that both services(llm-service & consumer-api) are up and running, connected through a Docker network.

- Stop the Docker Container
  ```
  make down
  ```
