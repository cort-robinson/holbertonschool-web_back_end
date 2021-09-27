const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const filePath = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(filePath)
    .then((data) => {
      res.send(`This is the list of our students\n${data.join('\n')}`);
    })
    .catch(() => {
      res.send('Cannot load the database');
    });
});

app.listen(1245, () => {
  console.log('Listening on port 1245');
});

module.exports = app;
