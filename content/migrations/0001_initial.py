# Generated by Django 4.1 on 2022-09-01 18:50

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=50, verbose_name="تایل")),
                ("text", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "date_added",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="تاریخ اضافه شدن",
                    ),
                ),
                ("to_other_pages", models.BooleanField(default=True)),
            ],
            options={"verbose_name": "خبر", "verbose_name_plural": "اخبار",},
        ),
    ]
