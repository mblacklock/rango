# Generated by Django 2.0.6 on 2018-06-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20180619_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
