<template>
  <div class="container">
    <div class="buttons-container">
      <v-btn>Adicionar Aluno</v-btn>
      <v-btn>Adicionar Nota</v-btn>
    </div>
    <TopThreeStudents />
    <TopTenStudents />
  </div>
</template>

<script setup>
import TopThreeStudents from "./TopThreeStudents.vue";
import TopTenStudents from "./TopTenStudents.vue";
</script>

<style scoped>
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
