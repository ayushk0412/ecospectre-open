# Generated by Django 3.1.1 on 2020-10-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceapp', '0007_auto_20201003_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desc',
            field=models.CharField(default="I find life better, and I'm happier, when things are nice and simple.", max_length=100),
        ),
    ]