export default function getStudentIdsSum(listOfStudent) {
  return listOfStudent.reduce((sum, student) => sum + student.id, 0);
}
