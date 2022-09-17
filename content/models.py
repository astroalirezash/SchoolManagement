from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.


class News(models.Model):
    banner = models.ImageField(
        upload_to='media/news/', max_length='200', default='media/defaults/news_banner.jpg'
    )
    title = models.CharField(
        verbose_name='تایل', max_length=50
    )
    text = RichTextField(
        null=True, blank=True
    )
    date_added = models.DateTimeField(
        verbose_name='تاریخ اضافه شدن', default=timezone.now
    )
    to_other_pages = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

    def __str__(self):
        return f'{self.title} | {self.date_added}'
