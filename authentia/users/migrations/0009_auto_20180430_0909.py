# Generated by Django 2.0.4 on 2018-04-30 14:09

from django.db import migrations, models
import helpers.files


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180429_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoenroll',
            name='file',
            field=models.ImageField(upload_to=helpers.files.upload_to_generic),
        ),
        migrations.AlterField(
            model_name='userdocument',
            name='file',
            field=models.FileField(upload_to=helpers.files.upload_to_generic),
        ),
    ]
