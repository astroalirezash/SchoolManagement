from django.contrib import admin

from .models import (
    Class,
    Grade,
    ReportCard,
    Lesson
)


# Register your models here.

admin.site.register(Class)
admin.site.register(Grade)
admin.site.register(ReportCard)
admin.site.register(Lesson)
