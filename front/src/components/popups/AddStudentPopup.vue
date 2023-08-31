<template>
  <v-dialog v-model="visible" class="add-student-popup">
    <v-card class="asp__card--container">
      <v-form ref="form">
        <v-card-title class="pl-0">Adicionar aluno</v-card-title>
        <v-card-text class="pa-0">
          <v-text-field
            label="Nome do aluno"
            v-model="name"
            :rules="[rules.required]"
          />
          <v-autocomplete
            label="Curso"
            v-model="course"
            item-value="value"
            item-title="name"
            :items="courses"
            :rules="[rules.required]"
          />
        </v-card-text>
        <v-card-actions class="aspc__actions--buttons">
          <v-btn border @click="close">Fechar</v-btn>
          <v-btn
            class="aspca__button--primary"
            :loading="loading"
            @click="addStudent"
            >Adicionar</v-btn
          >
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import apimock from "../../apimock/apimock.js";
import rules from "../../helpers/rules.js";

export default {
  props: {
    showAddStudentPopup: {
      required: true,
      type: Boolean,
    },
  },
  data() {
    return {
      course: "",
      courses: [
        { name: "Tarefas", value: "tasks" },
        { name: "Desafios", value: "challenges" },
        { name: "Projetos", value: "projects" },
      ],
      loading: false,
      name: "",
      rules,
    };
  },
  computed: {
    visible() {
      return this.showAddStudentPopup;
    },
  },
  methods: {
    async addStudent() {
      const { valid } = await this.$refs.form.validate();
      if (valid) {
        try {
          this.loading = true;
          await apimock.postStudent(this.name, this.course);
          this.close();
        } catch (error) {
          console.log(error);
        } finally {
          this.loading = false;
        }
      }
    },
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
