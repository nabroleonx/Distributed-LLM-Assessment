import { Router } from 'express';
import { sendQuery, getConversationHistory, getConversationDetails } from '../controllers/conversation.controllers';

const router = Router();

router.post('/query', sendQuery);
router.get('/history', getConversationHistory);
router.get('/:conversationId', getConversationDetails);

export default router;
