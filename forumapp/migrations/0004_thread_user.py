# Generated by Django 2.0.7 on 2018-08-02 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0003_auto_20180802_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]