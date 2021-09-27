const express = require('express');

// create an express app
const app = express();

// define a route handler for the default home page
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// start the express server
app.listen(1245, () => {
  console.log('Server started at http://localhost:1245');
});

module.exports = app;
