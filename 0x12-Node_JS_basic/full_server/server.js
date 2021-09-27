import express from 'express';

const app = express();

app.listen(1245, () => {
  console.log('server started');
});

export default app;
