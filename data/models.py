from django.db import models
from account.models import User

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(
    max_length=25,
    verbose_name='نام',
    null=False, blank=False
    )

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'
    
    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='نام',
        unique=True
        )
    students = models.ForeignKey(
        User,
        verbose_name='دانش آموزان',
        null=True, blank=True,
        on_delete=models.DO_NOTHING,
        related_name='students', 
        related_query_name='student'
    )
    teacher = models.ManyToManyField(
        User,
        verbose_name='معلمین',
        related_name='teachers',
        related_query_name='teacher'
    )

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'


# class Grade(models.Model):
#     classes = models.ForeignKey(Class, verbose_name='کلاس ها')
#     lessons = models.ForeignKey(Lesson, verbose_name='دروس')
#     students = models.ForeignKey(User, on_delete=models.DO_NOTHING())  # can i have a queryset here? for example class.students


# class ReportCard(models.Model):
#     student = models.ForeignKey(User, models.DO_NOTHING())
#     lessons = models.ManyToManyField(Lesson, on_delete=models.DO_NOTHING())
