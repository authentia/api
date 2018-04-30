# Generated by Django 2.0.4 on 2018-04-30 20:21

from django.db import migrations, models
import helpers.files


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0013_auto_20180430_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocument',
            name='file',
            field=models.FileField(upload_to=helpers.files.upload_to_generic),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='photo',
            field=models.ImageField(upload_to=helpers.files.upload_to_generic),
        ),
    ]
