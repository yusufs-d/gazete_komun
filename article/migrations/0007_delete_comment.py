# Generated by Django 3.2.7 on 2021-10-11 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20211011_2320'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]