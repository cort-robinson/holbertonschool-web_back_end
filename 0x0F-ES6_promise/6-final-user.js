import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

/**
 * The function should call the two other functions.
 * When the promises are all settled it should return
 * an array with the following structure:
 * [
 *  {
 *    status: status of the promise,
 *    value: value of the promise
 *  },
 *  ...
 * ]
 * @param {string} firstName first name of the user
 * @param {string} lastName last name of the user
 * @param {string} fileName file name of the photo
 * @returns {Promise<Array<{status: string, value: any}>>}
 */
export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]);
}
