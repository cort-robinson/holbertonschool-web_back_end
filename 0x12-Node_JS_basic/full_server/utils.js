import fs from 'fs';

export default async function readDatabase(path) {
  fs.access(path, (err) => {
    if (err) {
      throw Error('Cannot load the database');
    }
  });
  const data = await fs.promises.readFile(path, 'utf8');

  const lines = data.split('\n');
  if (lines[lines.length - 1] === '') {
    lines.pop();
  }

  const students = lines.map((line) => line.split(','));
  const fields = [...new Set(students.map((student) => student[3]))];
  fields.shift();

  const results = {};

  for (const field of fields) {
    const fieldStudents = students.filter((student) => student[3] === field);
    const fieldStudentsNames = fieldStudents.map((student) => student[0]);
    results[field] = fieldStudentsNames;
  }

  return results;
}
