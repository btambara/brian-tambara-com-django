<script setup lang="ts">
import Job from '../components/Job.vue';
import Education from '../components/Education.vue';
import Project from '../components/Project.vue';
</script>

<script lang="ts">
import { defineComponent } from 'vue';

const descriptionData = document.getElementById(
  'description',
) as HTMLInputElement | null;


let description = descriptionData?.textContent
if(description){
  description = description.replace(/^"(.+(?="$))"$/, '$1');
}


const jobData = document.getElementById(
  'jobs',
) as HTMLInputElement | null;

interface JobDict {
  company: string
  location: string
  from: string
  to: string
  title: string
  description: string
  notes: [string]
}

let jobs: JobDict[];
if(jobData != null && jobData.textContent != null){
  jobs = JSON.parse(jobData.textContent)
}

const educationData = document.getElementById(
  'degrees',
) as HTMLInputElement | null;

interface EducationDict {
  title: string
  school: string
  location: string
  from: string
  to: string
}

let degrees: EducationDict[];
if(educationData != null && educationData.textContent != null){
  degrees = JSON.parse(educationData.textContent)
}

const projectData = document.getElementById(
  'projects',
) as HTMLInputElement | null;

interface ProjectDict {
  title: string
  description: string
  url: string
  repo: string
}

let projects: ProjectDict[];
if(projectData != null && projectData.textContent != null){
  projects = JSON.parse(projectData.textContent)
}

export default defineComponent({
  name: "Resume",
  data: () => {
    return {
        description: description,
        jobs: jobs,
        degrees: degrees,
        projects: projects,
    }
  },
});
</script>


<template>
    <div class="row align-baseline">
      <a class="col-xl-2 icon-link" href="/">
        <i class="bi-house-door-fill" style="font-size: 2rem;">Home</i>
      </a>
    </div>
    <a class="col-xl icon-link" href="/media/Resume_Brian_Tambara.pdf">
          <i class="bi-file-earmark-arrow-down" style="font-size: 2rem;">Download</i>
    </a>
    <div class="container text-center">
        <h1 class="border-bottom">About me</h1>
        <div class="row justify-content-center">
          <div class="col col-xl-8 text-start">
            <p>{{ description }}</p>
          </div>
        </div>

        <h1 class="border-bottom">Professional Experience</h1>
        <Job v-for="job in jobs" :company="job.company" :location="job.location" :from="job.from" :to="job.to" :title="job.title" :description="job.description" :notes="job.notes"/>

        <h1 class="border-bottom">Education</h1>
        <Education v-for="degree in degrees" :title="degree.title" :school="degree.school" :location="degree.location" :from="degree.from" :to="degree.to" />

        <h1 class="border-bottom">Projects</h1>
        <Project v-for="project in projects" :title="project.title" :description="project.description" :url="project.url" :repo="project.repo" />
    </div>
</template>

<style scoped>
i::before{
  padding-right: 15px;
}
</style>
