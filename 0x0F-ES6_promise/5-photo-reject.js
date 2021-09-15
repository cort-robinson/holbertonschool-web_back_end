export default function uploadPhoto(fileName) {
  return Promise.reject(new Error(`${fileName} cannnot be processed`));
}
