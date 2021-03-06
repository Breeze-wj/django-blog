# Generated by Django 2.0 on 2020-06-15 10:22

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_about_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='loves',
            field=models.PositiveIntegerField(default=0, verbose_name='点赞量'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='excerpt',
            field=models.TextField(blank=True, max_length=230, verbose_name='摘要'),
        ),
    ]
