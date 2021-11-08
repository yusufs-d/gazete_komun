# Generated by Django 3.2.7 on 2021-11-08 15:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0016_about_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Makale',
        ),
        migrations.AlterField(
            model_name='about',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
    ]
