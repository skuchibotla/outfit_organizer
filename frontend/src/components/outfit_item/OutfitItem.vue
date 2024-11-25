<template>
  <div id="outfit-item">
    <OutfitItemUpload />
    <div id="outfit-item-select-container">
      <OutfitItemSelect selectType="type" v-model="typeRef" />
      <OutfitItemSelect selectType="color" v-model="colorRef" />
    </div>
  </div>
</template>

<script>
  import { ref } from 'vue';
  import OutfitItemSelect from './OutfitItemSelect.vue';
  import OutfitItemUpload from './OutfitItemUpload.vue';

  export default {
    name: 'OutfitItem',
    components: {
      OutfitItemSelect,
      OutfitItemUpload,
    },
    setup() {
      const typeRef = ref(null);
      const colorRef = ref(null);

      return { typeRef, colorRef };
    },
  }
</script>

<style>
  #outfit-item {
    height: 30%;
    width: 35%;
    min-width: 400px;
    min-height: 200px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    border: 1px solid grey;
    padding: 20px 20px;
    text-align: center;
  }

  #outfit-item-select-container {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    height: 160px;
  }
</style>
