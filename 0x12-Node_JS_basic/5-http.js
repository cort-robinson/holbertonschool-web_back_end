const http = require('http');
const countStudents = require('./3-read_file_async');

const filePath = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');
    countStudents(filePath)
      .then((data) => {
        res.write(`Number of students: ${data.students.length - 1}\n`);
        for (const field of data.fields) {
          const fieldStudents = data.students.filter((student) => student[3] === field);
          const fieldStudentsNames = fieldStudents.map((student) => student[0]);
          if (field === data.fields[data.fields.length - 1]) {
            res.write(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudentsNames.join(', ')}`);
          } else {
            res.write(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudentsNames.join(', ')}\n`);
          }
        }
        res.end();
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  }
});

app.listen(1245, () => {
  console.log('Server running at localhost:1245');
});

module.exports = app;
