<template>
  <div class="header">
    <div class="h__wrapper">
      <div class="hw__dnc-logo">
        <img :src="getImageUrl('logo_dnc')" alt="dnc_logo" />
      </div>
      <h1 class="hw__title">Ranking dos alunos</h1>
    </div>
  </div>
</template>

<script>
export default {
  setup() {
    const getImageUrl = () => {
      return new URL(`./assets/images/logo_dnc.webp`, import.meta.url).href;
    };
    return { getImageUrl };
  },
};
</script>

<style scoped lang="scss">
.header {
  height: 64px;
  background-color: var(--dark-background);
  position: relative;
  width: 100%;

  .h__wrapper {
    width: 100%;
    position: relative;
    padding: 16px 16px;
  }

  .hw__dnc-logo {
    display: flex;
  }

  .hw__dnc-logo img {
    max-height: 48px;
    max-width: 70px;
  }

  .hw__title {
    color: white;
    position: absolute;
    top: 50%;
    width: 100%;
    text-align: center;
    transform: translateY(-50%);
  }
}
</style>
