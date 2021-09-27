import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

export default (app) => {
  app.get('/', AppController.index);
  app.get('/students', StudentsController.index);
  app.get('/students/:major', StudentsController.index);
};
