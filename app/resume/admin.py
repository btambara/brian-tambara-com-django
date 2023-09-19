from django.contrib import admin

from .models import Education, Job, JobNote, Project, Resume


class JobAdmin(admin.ModelAdmin):
    list_display = ("company", "title", "work_from", "work_to")


admin.site.register(Resume)
admin.site.register(Job, JobAdmin)
admin.site.register(JobNote)
admin.site.register(Education)
admin.site.register(Project)
