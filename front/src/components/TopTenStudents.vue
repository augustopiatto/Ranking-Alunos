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
export default {
  data() {
    return {
      students: [
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
      ],
    };
  },
};
</script>

<style scoped>
.table {
  width: 400px;
}
</style>
