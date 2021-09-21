export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const typedArray = new Int8Array(buffer);
  typedArray[position] = value;
  return buffer;
}
