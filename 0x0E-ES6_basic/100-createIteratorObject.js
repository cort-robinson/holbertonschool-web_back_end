export default function createIteratorObject(report) {
  const iterable = [];
  for (const department of Object.keys(report.allEmployees)) {
    iterable.push(...report.allEmployees[department]);
  }
  return iterable;
}
