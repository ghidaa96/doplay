# Generated by Django 2.2.4 on 2020-11-06 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVShows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.TextField(default='no description provided'),
        ),
    ]