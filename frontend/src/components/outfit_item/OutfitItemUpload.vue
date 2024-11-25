
<template>
  <div>
    <Toast />
    <FileUpload
      name="file"
      url="http://127.0.0.1:3000/upload/123"
      accept="image/*"
      @error="onError"
      @progress="onProgress"
      @remove="onRemove"
      @before-upload="onBeforeUpload"
      @upload="onUpload"
      :maxFileSize="1000000">
      <template #empty>
        <span>Drag and drop image here to upload.</span>
      </template>
    </FileUpload>
  </div>
</template>

<script setup>
  import FileUpload from 'primevue/fileupload';
  import Toast from 'primevue/toast';
  import { useToast } from "primevue/usetoast";

  const toast = useToast();

  const onError = () => {
    toast.add({ severity: 'error', summary: 'Error', detail: 'An error occurred', life: 3000 });
  };

  const onProgress = () => {
    toast.add({ severity: 'info', summary: 'Progress', detail: 'Removing background...', life: 3000 });
  };

  const onRemove = () => {
    toast.add({ severity: 'info', summary: 'Remove', detail: 'Removed image', life: 3000 });
  };

  const onBeforeUpload = (event) => {
    event.formData.append('user_id', '123');
  };

  const onUpload = () => {
    toast.add({ severity: 'success', summary: 'Success', detail: 'Image uploaded', life: 3000 });
  };
</script>
