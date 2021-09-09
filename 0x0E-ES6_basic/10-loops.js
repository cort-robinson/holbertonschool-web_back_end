export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array.entries()) {
    const value = idx[1];
    // eslint-disable-next-line no-param-reassign
    array[idx[0]] = appendString + value;
  }

  return array;
}
