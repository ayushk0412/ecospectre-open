# Generated by Django 3.1.1 on 2020-10-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceapp', '0015_profile_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
