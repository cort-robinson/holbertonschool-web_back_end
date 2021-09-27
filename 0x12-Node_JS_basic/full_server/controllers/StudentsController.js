import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    res.status(200).write('This is the list of our students');
    readDatabase('database.csv')
      .then((data) => {
        for (const field of data) {
          res.write(`Number of students in ${field.name}. List: ${field}`);
        }
      });
  }

  static getAllStudentsByMajor(req, res) {
    res.status(200).write('This is the list of our students');
    readDatabase('database.csv')
      .then((data) => {
        for (const field of data) {
          res.write(`Number of students in ${field.name}. List: ${field}`);
        }
      });
  }
}
