# Generated by Django 3.1.1 on 2020-10-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceapp', '0011_auto_20201003_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
        migrations.AddField(
            model_name='profile',
            name='myimg',
            field=models.ImageField(null=True, upload_to='images\\'),
        ),
    ]