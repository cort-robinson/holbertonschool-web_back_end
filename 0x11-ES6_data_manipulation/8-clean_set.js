export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';
  let arr = Array.from(set);
  arr = arr.reduce((acc, curr) => {
    if (curr.startsWith(startString)) {
      acc.push(curr);
    }
    return acc;
  }, []);
  arr = arr.map((item) => item.replace(startString, ''));
  return arr.join('-');
}
