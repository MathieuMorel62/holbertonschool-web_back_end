function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.find(
        (gradeItem) => gradeItem.studentId === student.id,
      );
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}

export default updateStudentGradeByCity;
