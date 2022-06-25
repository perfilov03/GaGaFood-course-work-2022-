# Generated by Django 4.0.5 on 2022-06-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название ресторана')),
                ('description', models.TextField(verbose_name='О ресторане')),
                ('logo', models.ImageField(upload_to='restaurant', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
    ]