# Generated by Django 2.2.16 on 2022-06-20 07:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите жанр', max_length=100, unique=True, verbose_name='Жанр')),
                ('slug', models.SlugField(help_text='Укажите адрес', unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Укажите комментарий', max_length=1000, verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите жанр', max_length=100, unique=True, verbose_name='Жанр')),
                ('slug', models.SlugField(help_text='Укажите адрес', unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Напишите Отзыв', max_length=1000, verbose_name='Отзыв')),
                ('score', models.IntegerField(help_text='Укажите рейтинг', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка произведения')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Укажите дату', verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название произведения', max_length=100, verbose_name='Произведение')),
                ('year', models.PositiveSmallIntegerField(db_index=True, help_text='Укажите дату выхода', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2022)], verbose_name='Дата выхода произведения')),
                ('rating', models.IntegerField(null=True, verbose_name='Рейтинг')),
                ('description', models.CharField(blank=True, help_text='Укажите название произведения', max_length=1000, null=True, verbose_name='Произведение')),
                ('category', models.ForeignKey(blank=True, help_text='Укажите категорию', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Категория произведения')),
                ('genre', models.ManyToManyField(help_text='Укажите жaнры', related_name='titles', to='reviews.Genre', verbose_name='Жанры произведения')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('-year',),
            },
        ),
    ]