# Generated by Django 2.0.7 on 2018-08-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='name',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]
