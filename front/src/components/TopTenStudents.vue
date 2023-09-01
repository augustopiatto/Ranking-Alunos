<template>
  <v-table fixed-header class="table">
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

<style scoped lang="scss">
.table {
  width: 400px;
}
</style>
