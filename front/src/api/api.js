import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/api/",
});

const get = (url, params) => {
  return axiosInstance.get(url, { params });
};

const post = (url, params) => {
  return axiosInstance.post(url, { params });
};

const api = {
  getStudents() {
    return get("students/").then((response) => response.data);
  },
  getTop3Students() {
    return get("top-three-students/").then((response) => response.data);
  },
  getTop10Students(school) {
    return get("top-ten-students/", { school }).then(
      (response) => response.data
    );
  },
  postStudent(name, school) {
    return post("students/", { name, school }).then(
      (response) => response.data
    );
  },
  postGrade(studentId, school, grade) {
    return post("grades/", { studentId, school, grade }).then(
      (response) => response.data
    );
  },
};

export default api;
