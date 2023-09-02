<template>
  <div class="top-ten-students">
    <h2>Top 10 alunos por curso</h2>
    <v-table fixed-header>
      <thead>
        <tr>
          <th>Posição</th>
          <th>Nome do aluno</th>
          <th>Média final</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id">
          <td>{{ student.idx }}</td>
          <td>{{ student.name }}</td>
          <td>{{ student.final_score }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script>
import api from "../api/api.js";

export default {
  data() {
    return {
      students: [],
    };
  },
  async mounted() {
    try {
      this.students = await api.getTop10Students("data");
    } catch (error) {
      console.log(error);
    }
  },
};
</script>

<style lang="scss" scoped>
.top-ten-students {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
