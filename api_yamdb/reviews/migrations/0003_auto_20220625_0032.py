# Generated by Django 2.2.16 on 2022-06-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220620_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.CharField(blank=True, default=1, help_text='Укажите название произведения', max_length=1000, verbose_name='Произведение'),
            preserve_default=False,
        ),
    ]
