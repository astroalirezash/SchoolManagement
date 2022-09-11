from django.contrib import admin

from .models import (
    Class,
    Grade,
    ReportCard,
    Lesson,
    Score
)

from account.models import User

# Register your models here.


@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['student'].queryset = User.objects.filter(is_student=True)
         return super(ReportCardAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(Class)
admin.site.register(Grade)
admin.site.register(Lesson)
admin.site.register(Score)
