import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';
import app from '../server';

app.get('/', AppController.getHomepage);
app.get('/students', StudentsController.getAllStudents);
app.get('/students/:major', StudentsController.getAllStudentsByMajor);
