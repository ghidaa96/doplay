# Generated by Django 2.2.4 on 2020-11-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVShows', '0003_auto_20201108_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(error_messages={'unique': 'title should be unique'}, max_length=45, unique=True),
        ),
    ]
