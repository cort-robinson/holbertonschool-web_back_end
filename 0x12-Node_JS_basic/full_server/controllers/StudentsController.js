import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    res.write('This is the list of our students\n');
    readDatabase('database.csv')
      .then((data) => {
        for (const [field, names] of Object.entries(data)) {
          res.write(`Number of students in ${field}. List: ${names.join(', ')}`);
        }
        res.end();
      })
      .catch((err) => {
        res.status(500).write(err);
        res.end();
      });
  }

  static getAllStudentsByMajor(req, res) {
    if (req.params.major !== 'CS' && req.params.major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
    } else {
      const { major } = req.params;
      readDatabase('database.csv')
        .then((data) => {
          res.write(`List: ${data[major].join(', ')}`);
          res.end();
        }).catch((err) => {
          res.status(500).write(err);
          res.end();
        });
    }
  }
}
