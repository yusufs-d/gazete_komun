# Generated by Django 3.2.7 on 2021-10-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_rename_article_category_article_makale_türü'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='makale_türü',
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.CharField(choices=[('Siyaset-Yazı', 'Siyaset-Yazı'), ('Siyaset-Haber', 'Siyaset-Haber'), ('Spor-Yazı', 'Spor-Yazı'), ('Spor-Haber', 'Spor-Haber'), ('Müzik', 'Müzik'), ('Sinema', 'Sinema'), ('Edebiyat', 'Edebiyat'), ('Sahne Sanatları', 'Sahne Sanatları'), ('Görsel Sanatlar', 'Görsel Sanatlar'), ('Gezi Notu', 'Gezi Notu'), ('Çeviri', 'Çeviri')], default='Siyaset-Yazı', max_length=20, verbose_name='Makale Türü'),
        ),
    ]
