import express from 'express';

// create express app
const app = express();

app.listen(1245, () => {
  console.log('server started');
});

export default app;
