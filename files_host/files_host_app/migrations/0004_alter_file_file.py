# Generated by Django 3.2.9 on 2021-11-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files_host_app', '0003_auto_20211103_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
