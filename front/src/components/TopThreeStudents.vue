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
        { idx: 1, name: "Juliano", final_score: 10 },
        { idx: 2, name: "Godofredo", final_score: 9 },
        { idx: 3, name: "Julia", final_score: 8 },
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.table {
  width: 400px;
}
</style>
