from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Education, Job, JobNote, Project, Resume


def resume(request: HttpRequest) -> HttpResponse:
    resume = Resume.objects.first()

    jobs = list()
    for job in Job.objects.filter(resume=resume):
        notes = list()
        for job_note in JobNote.objects.filter(job=job):
            notes.append(job_note.note)
        jobs.append(
            {
                "company": job.company,
                "location": job.location,
                "title": job.title,
                "from": job.work_from,
                "to": job.work_to,
                "description": job.description,
                "notes": notes,
            }
        )

    projects = list()
    for project in Project.objects.filter(resume=resume):
        projects.append(
            {
                "title": project.title,
                "description": project.description,
                "url": project.url,
                "repo": project.repo_url,
            }
        )

    degrees = list()
    for education in Education.objects.filter(resume=resume):
        degrees.append(
            {
                "title": education.title,
                "school": education.school,
                "location": education.location,
                "from": education.school_from,
                "to": education.school_to,
            }
        )

    context = {
        "description": resume.description,
        "jobs": jobs,
        "projects": projects,
        "degrees": degrees,
    }
    return render(request, "resume.html", context=context)
