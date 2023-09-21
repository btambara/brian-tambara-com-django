<script setup lang="ts">
defineProps<{
    company: string,
    location: string,
    title: string,
    from: string,
    to: string,
    description: string,
    notes: [string],
}>()
</script>

<template>
    <div class="row">
      <div class="row"><h3 class="title">{{ title }}</h3></div>
      <div class="col text-xl-end"><h5 class="company">{{ company }}</h5></div>
      <div class="col col-xl-3 text-xl-start"><h5 class="location">{{ location }}</h5></div>
      <div class="row col-xl-3 text-xl-end"><h5 class="from">{{ from }}</h5></div>
      <div class="row col-xl text-xl-start"><h5 class="to">{{ to }}</h5></div>
      <div class="row justify-content-center">
        <div class="col col-xl-8 text-start">
          <p class="description">{{ description }}</p>
        </div>
      </div>
      <div v-if="notes" class="row justify-content-center">
        <div class="col col-xl-8 text-start">
          <li v-for="note in notes">{{ note }}</li>
        </div>
      </div>
    </div>
  </template>

  <style scoped>
  .company {
    font-weight: bold;
  }
  .title {
    font-weight: bold;
  }
  .location {
    font-style: italic;
  }
  </style>
