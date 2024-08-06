export interface Query {
  model: string;
  question: string;
}

export interface ConversationHistory {
  conversationId: string;
  history: {
    query: string;
    response: string;
  }[];
}

export interface ConversationBase {
  query: string;
  response: string;
}
