# Generated by Django 4.0.3 on 2022-06-13 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='POST')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='SLUG')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 6, 13, 22, 53, 25, 308297), verbose_name='CREATED DATE')),
                ('modified_date', models.DateTimeField(default=datetime.datetime(2022, 6, 13, 22, 53, 25, 308317), verbose_name='MODIFIED DATE')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ('-created_date',),
            },
        ),
    ]