export default function setFromArray(array) {
  const set = new Set();
  for (let i = 0; i < array.length; i += 1) {
    set.add(array[i]);
  }
  return set;
}
