# Generated by Django 4.1.1 on 2022-09-15 12:59

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название продукта')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Изоброжение')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Категория')),
            ],
        ),
    ]
