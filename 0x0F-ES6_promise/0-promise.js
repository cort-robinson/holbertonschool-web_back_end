export default function getResponseFromAPI() {
  return new Promise(((resolve) => {
    setTimeout(() => {
      resolve('Hello World');
    }, 2000);
  }));
}
