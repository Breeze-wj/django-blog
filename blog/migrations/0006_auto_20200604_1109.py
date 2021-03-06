# Generated by Django 2.0 on 2020-06-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200604_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='网站描述'),
        ),
        migrations.AddField(
            model_name='link',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='link_logo/%Y/%m/%d/', verbose_name='网站logo'),
        ),
    ]
