export default function updateStudentGradeByCity(students, city, newGrades) {
  const arr = students.filter((student) => student.location === city);
  arr.map((student) => {
    const updatedStudent = student;
    updatedStudent.grade = 'N/A';
    newGrades.forEach((newGrade) => {
      if (student.id === newGrade.studentId) {
        updatedStudent.grade = newGrade.grade;
      }
    });
    return updatedStudent;
  });
  return arr;
}
