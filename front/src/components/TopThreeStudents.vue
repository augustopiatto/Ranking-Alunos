<template>
  <div class="top-three-students">
    <h2>Top 3 geral de alunos</h2>
    <v-table fixed-header class="tts__table">
      <thead>
        <tr>
          <th>Posição</th>
          <th>Nome do aluno</th>
          <th>Média final</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in topThreeStudents" :key="student.id">
          <td>{{ student.idx }}</td>
          <td>{{ student.name }}</td>
          <td>{{ student.final_score }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script>
export default {
  props: {
    topThreeStudents: {
      required: true,
      type: Array,
    },
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
