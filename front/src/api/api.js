import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/api/",
});

const get = (url) => {
  return axiosInstance.get(url);
};

const post = (url) => {
  return axiosInstance.post(url);
};

const api = {
  getStudents() {
    return get("students/").then((response) => response.data);
  },
  getTop3Students() {
    return get("top-three-students/").then((response) => response.data);
  },
  getTop10Students() {
    return get("top-ten-students/").then((response) => response.data);
  },
  postStudent(name, course) {
    return post("students/", { name, course }).then(
      (response) => response.data
    );
  },
  postGrade(studentId, course, grade) {
    return post("grades/", { studentId, course, grade }).then(
      (response) => response.data
    );
  },
};

export default api;
