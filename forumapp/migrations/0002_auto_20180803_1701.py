# Generated by Django 2.0.7 on 2018-08-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]