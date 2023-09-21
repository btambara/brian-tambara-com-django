<script setup lang="ts">
import Introduction from '../components/Introduction.vue'
import ProfessionalProfile from './ProfessionalProfile.vue';
</script>

<template>
    <div class="row align-baseline">
        <a class="icon-link" href="/resume">
        <i class="bi-file-person-fill" style="font-size: 2rem;">Resume</i>
    </a>
    </div>

    <div class="container text-center">
        <div class="row align-items-center">
            <Introduction />
            <ProfessionalProfile />
        </div>
    </div>
</template>

<style scoped>
i::before{
  padding-right: 15px;
}
</style>
