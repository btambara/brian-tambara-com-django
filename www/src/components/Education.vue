<script setup lang="ts">
defineProps<{
    title: string,
    school: string,
    location: string,
    from: string,
    to: string,
}>()
</script>

<template>
    <div class="row">
        <div class="row"><h3 class="title">{{ title }}</h3></div>
        <div class="col text-end"><h5 class="school">{{ school }}</h5></div>
        <div class="col col-xl-2 text-xl-start"><h5 class="location">{{ location }}</h5></div>
        <div class="row col-xl-2 text-xl-end"><h5 class="from">{{ from }}</h5></div>
        <div class="row col-xl text-xl-start"><h5 class="to">{{ to }}</h5></div>
    </div>
  </template>

  <style scoped>
  .title {
    font-weight: bold;
  }
  .school {
    font-weight: bold;
  }
  .location {
    font-style: italic;
  }
  </style>
