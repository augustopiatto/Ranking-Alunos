const apimock = {
  getStudents() {
    return [
      { id: 1, name: "Roberto" },
      { id: 2, name: "Fredo" },
      { id: 3, name: "Roberta" },
      { id: 4, name: "Paulo" },
      { id: 5, name: "Tales" },
      { id: 6, name: "Ana" },
      { id: 7, name: "Núbia" },
      { id: 8, name: "Javanil" },
      { id: 9, name: "Toelison" },
      { id: 10, name: "Lara" },
      { id: 11, name: "Juliano" },
      { id: 12, name: "Godofredo" },
      { id: 13, name: "Julia" },
    ];
  },
  getTop3Students() {
    return [
      { idx: 1, name: "Juliano", final_score: 10 },
      { idx: 2, name: "Godofredo", final_score: 9 },
      { idx: 3, name: "Julia", final_score: 8 },
    ];
  },
  getTop10Students() {
    return [
      { idx: 1, name: "Roberto", final_score: 10 },
      { idx: 2, name: "Fredo", final_score: 9.9 },
      { idx: 3, name: "Roberta", final_score: 9.8 },
      { idx: 4, name: "Paulo", final_score: 9.7 },
      { idx: 5, name: "Tales", final_score: 9.6 },
      { idx: 6, name: "Ana", final_score: 9.5 },
      { idx: 7, name: "Núbia", final_score: 9.4 },
      { idx: 8, name: "Javanil", final_score: 9.3 },
      { idx: 9, name: "Toelison", final_score: 9.2 },
      { idx: 10, name: "Lara", final_score: 9.1 },
    ];
  },
  postStudent(name, course) {
    return;
  },
  postGrade(studentId, course, grade) {
    return;
  },
};

export default apimock;
