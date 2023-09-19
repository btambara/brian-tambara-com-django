from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Job, Resume


def resume(request: HttpRequest) -> HttpResponse:
    resume = Resume.objects.first()
    jobs = Job.objects.filter(resume=resume)

    context = {"resume_description": resume.description, "jobs": jobs}
    return render(request, "resume.html", context=context)
