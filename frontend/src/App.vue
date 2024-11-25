<template>
  <div>
    <OutfitItem />
  </div>
</template>

<script>
  import OutfitItem from './components/outfit_item/OutfitItem.vue';

  export default {
    name: 'App',
    components: {
      OutfitItem
    },
  }
</script>

<style>
  * {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  #app {
    margin-top: 60px;
  }
</style>
