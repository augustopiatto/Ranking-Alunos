<template>
  <v-dialog v-model="visible" class="add-student-popup">
    <v-card class="asp__card--container">
      <v-card-title class="pl-0">Adicionar aluno</v-card-title>
      <v-card-items>
        <v-text-field label="Nome do aluno" />
      </v-card-items>
      <v-card-actions class="aspc__actions--buttons">
        <v-btn border @click="close">Fechar</v-btn>
        <v-btn class="aspca__button--primary" @click="addStudent"
          >Adicionar</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    showAddStudentPopup: {
      required: true,
      type: Boolean,
    },
  },
  computed: {
    visible() {
      return this.showAddStudentPopup;
    },
  },
  methods: {
    addStudent() {},
    close() {
      this.$emit("close-add-student-popup");
    },
  },
};
</script>

<style scoped lang="scss">
.add-student-popup {
  max-width: 60%;

  .asp__card--container {
    padding: 24px;

    .aspc__actions--buttons {
      display: flex;
      justify-content: space-between;

      .aspca__button--primary {
        background-color: var(--blue);
        color: rgb(240, 240, 240);
      }
    }
  }
}
</style>
