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
    get("/top-3-students");
  },
  getTop10Students() {
    get("/top-10-students");
  },
  postStudent(name, course) {
    post("/students", { name, course });
  },
  postGrade(studentId, course, grade) {
    post("/grade", { studentId, course, grade });
  },
};
