<template>
  <div class="top-three-students">
    <h2>Top 3 geral de alunos</h2>
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
      this.students = await api.getTop3Students();
    } catch (error) {
      console.log(error);
    }
  },
};
</script>

<style lang="scss" scoped>
.top-three-students {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
