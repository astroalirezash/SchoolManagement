# Generated by Django 4.1 on 2022-08-31 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0003_reportcard_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score",
            name="quarter1",
            field=models.FloatField(
                default=0.0,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(20.0),
                ],
                verbose_name="میان ترم اول",
            ),
        ),
    ]