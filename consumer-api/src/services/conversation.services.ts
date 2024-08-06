import axios from "axios";

const PYTHON_API_URL = "http://localhost:8000";

export const sendQueryToPython = async (model: string, question: string) => {
  const response = await axios.post(`${PYTHON_API_URL}/query/`, {
    model,
    question,
  });
  return response.data;
};

export const fetchConversationHistory = async () => {
  const response = await axios.get(`${PYTHON_API_URL}/conversation/history`);
  return response.data;
};

export const fetchConversationDetails = async (conversationId: string) => {
  const response = await axios.get(
    `${PYTHON_API_URL}/conversation/${conversationId}`
  );
  return response.data;
};
