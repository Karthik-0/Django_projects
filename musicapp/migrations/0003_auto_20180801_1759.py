# Generated by Django 2.0.7 on 2018-08-01 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_band_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='title',
            new_name='name',
        ),
    ]