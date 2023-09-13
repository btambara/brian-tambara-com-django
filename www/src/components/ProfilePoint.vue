<script setup lang="ts">
defineProps<{ msg: string, description: string }>()
</script>

<template>
    <div class="col">
      <p class="message">{{ msg }}</p>
      <p class="description">{{ description }}</p>
    </div>
  </template>

  <style scoped>
  .message {
    font-weight: bold;
  }
  .description {
    font-style: italic;
  }
  </style>
