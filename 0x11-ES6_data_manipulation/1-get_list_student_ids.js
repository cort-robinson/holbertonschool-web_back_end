export default function getListStudentIds(objs) {
  if (Array.isArray(objs)) return objs.map((obj) => obj.id);
  return [];
}
