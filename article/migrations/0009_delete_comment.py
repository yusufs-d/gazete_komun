# Generated by Django 3.2.7 on 2021-10-11 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
