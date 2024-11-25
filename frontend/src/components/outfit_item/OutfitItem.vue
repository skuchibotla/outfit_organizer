<template>
  <div id="outfit-item-container">
    <OutfitItemSelect selectType="type" v-model="typeRef" />
    <OutfitItemSelect selectType="color" v-model="colorRef" />
    <OutfitItemUpload />
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
  #outfit-item-container {
    width: 25%;
    min-width: 250px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    border: 1px solid grey;
    padding: 20px 20px;
    text-align: center;
  }
</style>
