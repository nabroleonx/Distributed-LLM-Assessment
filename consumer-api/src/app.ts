import express from 'express';
import conversationRoutes from './routes/conversation.routes';

const app = express();

app.use('/api/conversations', conversationRoutes);

export default app;
