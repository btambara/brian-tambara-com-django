from django.db import models


class Resume(models.Model):
    description = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return "Brian Tambara - Software Engineer"


class Job(models.Model):
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE)
    company = models.CharField(blank=False, null=False, max_length=50)
    location = models.CharField(blank=False, null=False, max_length=50)
    title = models.CharField(blank=False, null=False, max_length=50)
    work_from = models.DateField()
    work_to = models.DateField()
    description = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.company} - {self.title}"


class JobNote(models.Model):
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    note = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.job} - {self.pk}"


class Project(models.Model):
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=50)
    description = models.TextField(blank=False, null=False)
    url = models.URLField(blank=True, null=True)
    repo_url = models.URLField(blank=False, null=False)

    def __str__(self) -> str:
        return self.title


class Education(models.Model):
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=50)
    school = models.CharField(blank=False, null=False, max_length=50)
    location = models.CharField(blank=False, null=False, max_length=50)
    school_from = models.DateField()
    school_to = models.DateField()

    def __str__(self) -> str:
        return f"{self.title} - {self.school}"
