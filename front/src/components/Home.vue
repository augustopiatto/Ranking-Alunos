<template>
  <div class="container">
    <div class="buttons-container">
      <v-btn @click="openAddStudentPopup">Adicionar Aluno</v-btn>
      <v-btn @click="openAddGradePopup">Adicionar Nota</v-btn>
    </div>
    <TopThreeStudents />
    <TopTenStudents />
    <AddGradePopup v-if="showAddGradePopup" @close="closeAddGradePopup" />
    <AddStudentPopup
      v-if="showAddStudentPopup"
      :showAddStudentPopup="showAddStudentPopup"
      @close="closeAddStudentPopup"
    />
  </div>
</template>

<script>
import AddGradePopup from "./popups/AddGradePopup.vue";
import AddStudentPopup from "./popups/AddStudentPopup.vue";
import TopThreeStudents from "./TopThreeStudents.vue";
import TopTenStudents from "./TopTenStudents.vue";

export default {
  components: {
    AddGradePopup,
    AddStudentPopup,
    TopThreeStudents,
    TopTenStudents,
  },
  data() {
    return {
      showAddGradePopup: false,
      showAddStudentPopup: false,
    };
  },
  methods: {
    closeAddGradePopup() {
      this.showAddGradePopup = false;
    },
    closeAddStudentPopup() {
      this.showAddStudentPopup = false;
    },
    openAddGradePopup() {
      this.showAddGradePopup = true;
    },
    openAddStudentPopup() {
      this.showAddStudentPopup = true;
    },
  },
};
</script>

<style scoped lang="scss">
.container {
  height: calc(100vh - 64px /** header */);
  padding: 32px 0;
  max-width: 640px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}

.buttons-container {
  width: 100%;
  display: flex;
  justify-content: space-between;
}
</style>
