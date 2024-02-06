from django.contrib import admin
from mentor.models import Course, Mentor

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
