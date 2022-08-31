from django.contrib import admin

from .models import (
    Class,
    Grade,
    ReportCard,
    Lesson,
    Score
)


# Register your models here.

admin.site.register(Class)
admin.site.register(Grade)
admin.site.register(ReportCard)
admin.site.register(Lesson)
admin.site.register(Score)
