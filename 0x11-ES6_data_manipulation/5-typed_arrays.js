export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const dataView = new DataView(buffer);
  const typedArray = new Int8Array(buffer);
  if (position < length) {
    typedArray[position] = value;
  } else throw new Error('Position outside range');
  return dataView;
}
