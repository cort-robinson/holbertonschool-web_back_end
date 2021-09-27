import express from 'express';
import index from './routes/index';

// create express app
const app = express();

index(app);

app.listen(1245, () => {
  console.log('server started');
});

export default app;
