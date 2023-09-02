<template>
  <div class="home">
    <div class="h__buttons--container">
      <v-btn @click="openAddStudentPopup" class="hb__button"
        >Adicionar Aluno</v-btn
      >
      <v-btn @click="openAddGradePopup" class="hb__button"
        >Adicionar Nota</v-btn
      >
    </div>
    <TopThreeStudents />
    <TopTenStudents />
    <AddGradePopup
      v-if="showAddGradePopup"
      :show-add-grade-popup="showAddGradePopup"
      @close-add-grade-popup="closeAddGradePopup"
    />
    <AddStudentPopup
      v-if="showAddStudentPopup"
      :show-add-student-popup="showAddStudentPopup"
      @close-add-student-popup="closeAddStudentPopup"
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
.home {
  height: calc(100vh - 64px /** header */);
  padding: 32px 0;
  max-width: 640px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;

  .h__buttons--container {
    width: 100%;
    display: flex;
    justify-content: space-between;

    .hb__button {
      background-color: var(--darker-blue);
      color: white;
      border-radius: 12px;
      padding: 16px 32px;
      height: auto;
    }
  }
}
</style>
