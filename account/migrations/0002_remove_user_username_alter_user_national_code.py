# Generated by Django 4.1 on 2022-08-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.CharField(max_length=10, unique=True, verbose_name='کد ملی'),
        ),
    ]
