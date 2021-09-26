const http = require('http');

// create http server
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
});

// listen http server
app.listen(1245, () => {
  console.log('Hello Holberton School!');
});

module.exports = app;
