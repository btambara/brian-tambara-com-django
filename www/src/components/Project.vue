<script setup lang="ts">
defineProps<{
    title: string,
    description: string,
    url: string,
    repo: string,
}>()
</script>

<template>
    <div class="container">
        <div class="row">
            <div class="row">
                <h3 class="title">{{ title }}</h3>
            </div>
            <div class="row">
                <p class="description">{{ description }}</p>
            </div>
            <div class="col text-end">
                <a class="icon-link" :href="url">
                    <i class="bi-link" style="font-size: 2rem;"></i>
                </a>
            </div>
            <div class="col text-start">
                <a class="icon-link" :href="repo">
                    <i class="bi-github" style="font-size: 2rem;"></i>
                </a>
            </div>
        </div>
    </div>
  </template>

  <style scoped>
  .title {
    font-weight: bold;
  }
  .description {
    font-style: italic;
  }
  </style>
