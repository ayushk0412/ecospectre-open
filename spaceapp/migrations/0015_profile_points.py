# Generated by Django 3.1.1 on 2020-10-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceapp', '0014_auto_20201003_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
