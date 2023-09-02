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
    <TopThreeStudents :top-three-students="topThreeStudents" />
    <TopTenStudents
      :top-ten-students="topTenStudents"
      @update="getTopTenStudents"
    />
    <AddGradePopup
      v-if="showAddGradePopup"
      :show-add-grade-popup="showAddGradePopup"
      @close-add-grade-popup="closeAddGradePopup"
      @update="getBothTopStudentsApi"
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
import api from "../api/api.js";

export default {
  components: {
    AddGradePopup,
    AddStudentPopup,
    TopThreeStudents,
    TopTenStudents,
  },
  data() {
    return {
      params: "data",
      showAddGradePopup: false,
      showAddStudentPopup: false,
      topTenStudents: [],
      topThreeStudents: [],
    };
  },
  async mounted() {
    await this.getBothTopStudentsApi();
  },
  methods: {
    closeAddGradePopup() {
      this.showAddGradePopup = false;
    },
    closeAddStudentPopup() {
      this.showAddStudentPopup = false;
    },
    async getTopTenStudents(param) {
      if (param) {
        this.params = param;
      }
      try {
        this.topTenStudents = await api.getTop10Students(this.params);
      } catch (error) {
        console.log(error);
      }
    },
    async getTopThreeStudents() {
      try {
        this.topThreeStudents = await api.getTop3Students();
      } catch (error) {
        console.log(error);
      }
    },
    async getBothTopStudentsApi() {
      Promise.all([this.getTopThreeStudents(), this.getTopTenStudents()]);
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
  height: auto;
  padding: 32px 16px;
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

  @media (max-width: 640px) {
    .h__buttons--container {
      flex-direction: column;
      gap: 16px;
    }
  }
}
</style>
