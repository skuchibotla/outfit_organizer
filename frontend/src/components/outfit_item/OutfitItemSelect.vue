<template>
  <div :class="`outfit-item-${props.selectType}`">
    <Select
      v-model="selectRef"
      :options="options"
      showClear
      checkmark
      optionLabel="label"
      optionValue="value"
      :placeholder="`Select a ${props.selectType}`"
      :highlightOnSelect="false"
    >
      <template #footer>
        <Button label="Add New" fluid severity="secondary" text size="small" icon="pi pi-plus"></Button>
      </template>
    </Select>
  </div>
</template>

<script setup>
  import Button from 'primevue/button';
  import Select from 'primevue/select';
  import { computed, defineProps, ref } from 'vue';

  const props = defineProps({
    selectType: {
      type: String,
      required: true,
    },
  });

  const { selectType } = props;
  const selectRef = ref(null);

  const colorOptions = ref([
    { label: 'Red', value: 'red' },
    { label: 'Green', value: 'green' },
    { label: 'Blue', value: 'blue' }
  ]);

  const typeOptions = ref([
    { label: 'T-Shirt', value: 'tshirt' },
    { label: 'Tank Top', value: 'tanktop' },
    { label: 'Blouse', value: 'blouse' }
  ]);

  const options = computed(() =>
    selectType === 'type' ? typeOptions.value : colorOptions.value
  );
</script>
