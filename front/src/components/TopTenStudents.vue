<template>
  <div class="top-ten-students">
    <h2>Top 10 alunos por curso</h2>
    <div>
      <div class="tts__buttons--container">
        <div class="ttsb__data-button" @click="updateTable('data')">
          <div class="ttsb__button">Dados</div>
          <div class="ttsb__triangle"></div>
        </div>
        <div class="ttsb__tech-button" @click="updateTable('technology')">
          <div class="ttsb__button">Tecnologia</div>
          <div class="ttsb__triangle"></div>
        </div>
        <div class="ttsb__product-button" @click="updateTable('product')">
          <div class="ttsb__button">Produto</div>
          <div class="ttsb__triangle"></div>
        </div>
      </div>
      <v-table fixed-header>
        <thead>
          <tr>
            <th>Posição</th>
            <th>Nome do aluno</th>
            <th>Média final</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in topTenStudents" :key="student.id">
            <td>{{ student.idx }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.final_score }}</td>
          </tr>
        </tbody>
      </v-table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    topTenStudents: {
      required: true,
      type: Array,
    },
  },
  methods: {
    updateTable(param) {
      this.$emit("update", param);
    },
  },
};
</script>

<style lang="scss" scoped>
.top-ten-students {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;

  .tts__buttons--container {
    display: flex;
    margin-bottom: -8px;

    .ttsb__data-button {
      display: flex;
      cursor: pointer;
    }

    .ttsb__tech-button {
      display: flex;
      margin-left: -16px;
      cursor: pointer;
    }

    .ttsb__product-button {
      display: flex;
      margin-left: -16px;
      cursor: pointer;
    }

    .ttsb__button {
      background-color: var(--darker-blue);
      border-radius: 4px 0 0 0;
      padding: 4px 8px;
      color: white;
      max-height: 40px;
      border-left: solid 1px black;
      border-top: solid 1px black;
    }

    .ttsb__triangle {
      height: 0;
      width: 0;
      border-bottom: 40px solid var(--darker-blue);
      border-right: 40px solid transparent;
    }
  }
}
</style>
