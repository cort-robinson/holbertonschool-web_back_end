export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';
  return Array.from(set)
    .map((item) => (typeof item === 'string' && item.startsWith(startString) ? item.slice(startString.length) : ''))
    .filter((item) => item !== '')
    .join('-');
}
