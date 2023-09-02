<template>
  <v-dialog v-model="isVisible" class="add-student-popup" persistent>
    <v-card class="asp__card--container">
      <v-form ref="form">
        <v-card-title class="pl-0 aspc__title">Adicionar aluno</v-card-title>
        <v-card-text class="pa-0">
          <v-text-field
            label="Nome do aluno"
            v-model="name"
            :rules="[rules.required]"
          />
        </v-card-text>
        <v-card-actions class="aspc__actions--buttons">
          <v-btn class="aspca__button--secondary" border @click="close"
            >Fechar</v-btn
          >
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
import api from "../../api/api.js";
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
      loading: false,
      name: "",
      rules,
      visible: true,
    };
  },
  computed: {
    isVisible() {
      return this.showAddStudentPopup;
    },
  },
  methods: {
    async addStudent() {
      const { valid } = await this.$refs.form.validate();
      if (valid) {
        try {
          this.loading = true;
          await api.postStudent(this.name);
          this.close();
          this.$emit("update");
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
    background-color: var(--light-background);

    .aspc__title {
      font-size: 20px;
      font-weight: 800;
      color: var(--darker-blue);
    }

    .aspc__actions--buttons {
      display: flex;
      justify-content: space-between;

      .aspca__button--primary {
        background-color: var(--darker-blue);
        color: white;
      }

      .aspca__button--secondary {
        border: 1px solid black;
      }
    }
  }
}
</style>
