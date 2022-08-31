from multiprocessing import Manager
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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


class Grade(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='نام'
    )
    classes = models.ForeignKey(
        Class,
        verbose_name='کلاس ها',
        on_delete=models.DO_NOTHING,
        # related_name='classes'
    )
    lessons = models.ForeignKey(
        Lesson,
        verbose_name='دروس',
        on_delete=models.DO_NOTHING,
        # related_name='lessons'
    )
    students = models.ForeignKey(
        User,
        verbose_name='دانش آموزان',
        on_delete=models.DO_NOTHING,
        # related_name='students'
    )

    class Meta:
        verbose_name = 'پایه'
        verbose_name_plural = 'پایه ها'
    
    def __str__(self):
        return self.name


class ReportCard(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='دانش آموز'
    )
    year = models.CharField(
        verbose_name='سال تحصیلی',
        max_length=10
    )

    class Meta:
        verbose_name = 'کارنامه'
        verbose_name_plural = 'کارنامه ها'
    
    def __str__(self):
        return f'{self.student.full_name()} | {self.year}'


class Score(models.Model):
    quarter1 = models.FloatField(
        verbose_name='میان ترم اول',
        default=0.0,
        validators=[
            MinValueValidator(0.0), MaxValueValidator(20.0)
        ]
    )
    quarter2 = models.FloatField(
        verbose_name='ترم اول',
        default=0.0,
        validators=[
            MinValueValidator(0.0), MaxValueValidator(20.0)
        ]
    )
    quarter3 = models.FloatField(
        verbose_name='میان ترم دوم',
        default=0.0,
        validators=[
            MinValueValidator(0.0), MaxValueValidator(20.0)
        ]
    )
    quarter4 = models.FloatField(
        verbose_name='خرداد',
        default=0.0,
        validators=[
            MinValueValidator(0.0), MaxValueValidator(20.0)
        ]
    )
    lesson = models.ForeignKey(
        Lesson,
        verbose_name='نام درس', 
        on_delete=models.PROTECT
    )
    rcard = models.ForeignKey(
        ReportCard,
        verbose_name='کارنامه',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'نمره درس'
        verbose_name_plural = 'نمرات دروس'
    
    def __str__(self):
        return f'{self.rcard.student.full_name()} | {self.lesson}'
