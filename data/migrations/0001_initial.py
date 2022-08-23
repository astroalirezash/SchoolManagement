# Generated by Django 4.1 on 2022-08-23 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="نام"),
                ),
                (
                    "students",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="students",
                        related_query_name="student",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="دانش آموزان",
                    ),
                ),
                (
                    "teacher",
                    models.ManyToManyField(
                        related_name="teachers",
                        related_query_name="teacher",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="معلمین",
                    ),
                ),
            ],
            options={"verbose_name": "کلاس", "verbose_name_plural": "کلاس ها",},
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25, verbose_name="نام")),
            ],
            options={"verbose_name": "درس", "verbose_name_plural": "دروس",},
        ),
        migrations.CreateModel(
            name="ReportCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lessons",
                    models.ManyToManyField(to="data.lesson", verbose_name="دروس"),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="دانش آموز",
                    ),
                ),
            ],
            options={"verbose_name": "کارنامه", "verbose_name_plural": "کارنامه ها",},
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="نام")),
                (
                    "classes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="data.class",
                        verbose_name="کلاس ها",
                    ),
                ),
                (
                    "lessons",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="data.lesson",
                        verbose_name="دروس",
                    ),
                ),
                (
                    "students",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="دانش آموزان",
                    ),
                ),
            ],
            options={"verbose_name": "پایه", "verbose_name_plural": "پایه ها",},
        ),
    ]