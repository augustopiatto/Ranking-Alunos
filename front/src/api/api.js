import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "localhost:5176/api",
});

const get = (url) => {
  return axiosInstance.get(url);
};

const post = (url) => {
  return axiosInstance.post(url);
};

export const api = {
  getStudents() {
    get("/students");
  },
  getTop3Students() {
    get("/top-three-students");
  },
  getTop10Students() {
    get("/top-ten-students");
  },
  postStudent(name, course) {
    post("/students", { name, course });
  },
  postGrade(studentId, course, grade) {
    post("/grades", { studentId, course, grade });
  },
};
