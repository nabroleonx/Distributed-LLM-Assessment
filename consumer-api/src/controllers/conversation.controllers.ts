import { Request, Response } from 'express';
import {
  sendQueryToPython,
  fetchConversationHistory,
  fetchConversationDetails,
} from '../services/conversation.services';

export const sendQuery = async (req: Request, res: Response) => {
  const { model, question } = req.body;
  try {
    const response = await sendQueryToPython(model, question);
    res.status(200).json(response);
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while sending the query' });
  }
};

export const getConversationHistory = async (req: Request, res: Response) => {
  try {
    const history = await fetchConversationHistory();
    res.status(200).json(history);
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while fetching conversation history' });
  }
};

export const getConversationDetails = async (req: Request, res: Response) => {
  const { conversationId } = req.params;
  try {
    const details = await fetchConversationDetails(conversationId);
    res.status(200).json(details);
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while fetching conversation details' });
  }
};
