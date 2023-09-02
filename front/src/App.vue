<template>
  <div class="app-body">
    <Header />
    <main>
      <Home />
    </main>
  </div>
</template>

<script setup>
import Header from "./Header.vue";
import Home from "./components/Home.vue";
</script>

<style lang="scss" scoped>
.app-body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
</style>
