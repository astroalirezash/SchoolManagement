from django.db import models
from account.models import User

# Create your models here.


class Lesson(models.Model):
    name = models.CharField

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'


class Class(models.Model):
    students = models.ForeignKey
    teacher = models.ManyToManyField

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'


class Grade(models.Model):
    classes = models.ForeignKey(Class, verbose_name='کلاس ها')
    lessons = models.ForeignKey(Lesson, verbose_name='دروس')
    students = models.ForeignKey(User, on_delete=models.DO_NOTHING())  # can i have a queryset here? for example class.students


class ReportCard(models.Model):
    student = models.ForeignKey(User, models.DO_NOTHING())
    lessons = models.ManyToManyField(Lesson, on_delete=models.DO_NOTHING())
