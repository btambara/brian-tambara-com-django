<script setup lang="ts">
import ProfilePoint from '../components/ProfilePoint.vue';
</script>

<template>
    <div class="col">
        <i class="bi-terminal" style="font-size: 2rem;"></i>
        <ProfilePoint msg="View time consuming processes and system shortfalls as opportunities to innovate" description="Developed applications to automate time-consuming tasks, increase operational efficiency, and eliminate errors caused by manual intervention."/>
        <i class="bi-file-code" style="font-size: 2rem;"></i>
        <ProfilePoint msg="Continuously learn and adapt to rapidly evolving and emerging technologies" description="Automated process for backing up major studio projects at Deluxe Media. Learned Python and PHP to develop a user-friendly and intuitive web interface."/>
        <i class="bi-wrench" style="font-size: 2rem;"></i>
        <ProfilePoint msg="Managed the migration from Python 2 to Python 3 for a client application." description="Refactored codebase to reflect the latest Python 3 changes. Updated all libraries for compatibility. Added typing to most of the codebase. Wrote unit tests to confirm that the changes work correctly."/>
    </div>
</template>
