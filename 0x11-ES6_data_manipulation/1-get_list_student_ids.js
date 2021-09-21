export default function getListStudentIds(objs) {
  const arr = [];
  if (Array.isArray(objs)) {
    for (let i = 0; i < objs.length; i += 1) {
      arr.push(objs[i].id);
    }
  }
  return arr;
}
