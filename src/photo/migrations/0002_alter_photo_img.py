# Generated by Django 3.2.6 on 2021-08-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.FileField(upload_to='images'),
        ),
    ]