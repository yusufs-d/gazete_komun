# Generated by Django 3.2.7 on 2021-10-31 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20211029_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_superarticle',
            field=models.BooleanField(default=0, verbose_name='Haftanın Makalesi Yap'),
        ),
    ]