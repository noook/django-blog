# Generated by Django 2.1.2 on 2018-11-24 14:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
